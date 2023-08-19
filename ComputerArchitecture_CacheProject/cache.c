/*
 * cache.c
 *
 * 20493-01 Computer Architecture
 * Term Project on Implentation of Cache Mechanism
 *
 * Skeleton Code Prepared by Prof. HyungJune Lee
 * Nov 15, 2021
 *
 */


#include <stdio.h>
#include <string.h>
#include "cache_impl.h"

extern int num_cache_hits;
extern int num_cache_misses;

extern int num_bytes;
extern int num_access_cycles;

extern int global_timestamp;

cache_entry_t cache_array[CACHE_SET_SIZE][DEFAULT_CACHE_ASSOC]; // cache_array
int memory_array[DEFAULT_MEMORY_SIZE_WORD]; // memory_array


/* DO NOT CHANGE THE FOLLOWING FUNCTION */
void init_memory_content() {
    unsigned char sample_upward[16] = {0x001, 0x012, 0x023, 0x034, 0x045, 0x056, 0x067, 0x078, 0x089, 0x09a, 0x0ab, 0x0bc, 0x0cd, 0x0de, 0x0ef};
    unsigned char sample_downward[16] = {0x0fe, 0x0ed, 0x0dc, 0x0cb, 0x0ba, 0x0a9, 0x098, 0x087, 0x076, 0x065, 0x054, 0x043, 0x032, 0x021, 0x010};
    int index, i=0, j=1, gap = 1;
    
    for (index=0; index < DEFAULT_MEMORY_SIZE_WORD; index++) {
        memory_array[index] = (sample_upward[i] << 24) | (sample_upward[j] << 16) | (sample_downward[i] << 8) | (sample_downward[j]);
        if (++i >= 16)
            i = 0;
        if (++j >= 16)
            j = 0;
        
        if (i == 0 && j == i+gap)
            j = i + (++gap);
            
        printf("mem[%d] = %#x\n", index, memory_array[index]);
    }
}   

/* DO NOT CHANGE THE FOLLOWING FUNCTION */
void init_cache_content() {
    int i, j;
    
    for (i=0; i<CACHE_SET_SIZE; i++) {
        for (j=0; j < DEFAULT_CACHE_ASSOC; j++) {
            cache_entry_t *pEntry = &cache_array[i][j];
            pEntry->valid = 0;
            pEntry->tag = -1;
            pEntry->timestamp = 0;
        }
    }
}

/* DO NOT CHANGE THE FOLLOWING FUNCTION */
/* This function is a utility function to print all the cache entries. It will be useful for your debugging */
void print_cache_entries() {
    int i, j, k;
    
    for (i=0; i<CACHE_SET_SIZE; i++) {
        printf("[Set %d] ", i);
        for (j=0; j <DEFAULT_CACHE_ASSOC; j++) {
            cache_entry_t *pEntry = &cache_array[i][j];
            printf("V: %d Tag: %#x Time: %d Data: ", pEntry->valid, pEntry->tag, pEntry->timestamp);
            for (k=0; k<DEFAULT_CACHE_BLOCK_SIZE_BYTE; k++) {
                printf("%#x(%d) ", pEntry->data[k], k);
            }
            printf("\t");
        }
        printf("\n");
    }
}

int cache_return(cache_entry_t *pEntry, char type, int byte_offset){
    int end = 0; // end means how many bytes will be read
    switch(type){
        case 'b': // if data_type is 'b' byte
            num_bytes++; // 1 byte
            end = 1; // 1 byte read
            break;
        case 'h': // if data_type is 'h' half word
            num_bytes+=2; // 2 bytes
            end = 2; // 2 bytes read
            break;
        case 'w': // if data_type is 'w' word
            num_bytes+=4; // 4 bytes
            end = 4; // 4 bytes read
            break;
        default: 
            return -1; // if not found return -1
    }
    int result=0; // value_returned to retrieve data
    for(int i=0; i<end; i++){
        result+=((pEntry->data[byte_offset+i])&0xff)<<(i*8);
        // (pEntry->data[byte_offset+i]) means ith cache data
        // &0xff to get only real cahce data
        // <<(i*8) left shift i*8
    }
    return result; // add each digit of cache_data
}

int check_cache_data_hit(int addr, char type) { 

    /* Fill out here */
    int block_addr = (addr / DEFAULT_CACHE_BLOCK_SIZE_BYTE); // block address
    int cache_index=block_addr % CACHE_SET_SIZE; // set number of addr
    int tag_num = block_addr / CACHE_SET_SIZE; // tag number of addr
    int byte_offset = addr % DEFAULT_CACHE_BLOCK_SIZE_BYTE; // byte_offset

    for(int j=0; j<DEFAULT_CACHE_ASSOC; j++){ // check if cache data hit
        cache_entry_t *pEntry = &cache_array[cache_index][j]; // pEntry indicates cahce_index set's j cache_entry
        if(pEntry->valid == 1){ // if it is valid, cache exists in that entry
            if(pEntry->tag == tag_num){ // if tag_num is same, cache hit
                num_cache_hits++; // hit counter up
                return cache_return(pEntry, type, byte_offset); // return that hit cahce value
            }
        }
            
    }

    /* Return the data */
    return -1; // if miss return -1 value
}

int find_entry_index_in_set(int cache_index) {
   if (DEFAULT_CACHE_ASSOC == 1) return 0; //if it is directed mapped cache, entry index is 0

   int j = 0; //variable for loop

   /* Check if there exists any empty cache space by checking 'valid' */
   for (j = 0; j<DEFAULT_CACHE_ASSOC; j++) {
      if (cache_array[cache_index][j].valid == 0) return j;  
      //if cache_array[cache_index][j]'s valid is 0, return that j(=entry index)
   }

   /* Otherwise, search over all entries to find the least recently used entry by checking 'timestamp' */
   int min_timestamp = global_timestamp; //min_timestamp means the smallest timestamp in cache
   int entry_index = 0; //entry_index variable was initialized to zero

                   //Go around the loop and find the smallest timestamp
   for (j = 0; j<DEFAULT_CACHE_ASSOC; j++) {
      if (cache_array[cache_index][j].timestamp <= min_timestamp) { //if cache_array[cache_index][j].timestamp is smaller than min_timestamp
         min_timestamp = cache_array[cache_index][j].timestamp; //that cache_array[cache_index][j].timestamp becomes min_timestamp
         entry_index = j;   //The variable(j) containing the smallest timestamp was stored in the entry_index

      }
   }
}


int access_memory(int addr, char type) {
   /* void *addr: addr is byte address, whereas your main memory address is word address due to 'int memory_array[]' */

   /* Get the entry index by invoking find_entry_index_in_set() for copying to the cache */
   int cache_index = (addr / DEFAULT_CACHE_BLOCK_SIZE_BYTE) % CACHE_SET_SIZE; 
   //int cache_index = ( addr / 8 ) % set size(if directed mapped cache, it will be 4)
   
   int entry_index = find_entry_index_in_set(cache_index);
   //Call the function find_entry_index_in_set, copy it from memory and get an entry to update

   /*update the cache_miss number*/
   num_cache_misses++;

   /* Fetch the data from the main memory and copy them to the cache */
   int j; //variable for loop
   int block_addr = (addr / DEFAULT_CACHE_BLOCK_SIZE_BYTE); //block address = addr(that we want to access) / 8
   int byte_offset = addr % DEFAULT_CACHE_BLOCK_SIZE_BYTE; //byte_offset = addr(that we want to access) % 8
   int word_index = block_addr * DEFAULT_CACHE_BLOCK_SIZE_BYTE / WORD_SIZE_BYTE;  //word_index = blockaddress * 8 / 4
   int tag_num = block_addr / CACHE_SET_SIZE; //tag number = block address / cache set size
   int value_returned;  //value that will be return into the retrieve_data function

   // Update the cache's valid, tag, timestamp one by one
   cache_entry_t *pEntry = &cache_array[cache_index][entry_index]; //*pEntry pointer points the address of cache_array[cache_index][entry_index]
   pEntry->valid = 1; //update cache_array[cache_index][entry_index]'s valid into 1

   pEntry->tag = tag_num; //copy the tag number

   global_timestamp++; // update global_timestamp + 1
   pEntry->timestamp = global_timestamp; //  Update the timestamp
   
                                // Update the cache data
                                //Save the 2 words of memory_array in cache_array - using pointer
   int memory1 = memory_array[word_index]; //Beginning part of the memory that will be copy
   int memory2 = memory_array[word_index + 1]; //End part of the memory that will be copy

   char *p = (char*)&memory1; //Point the starting address of the memory1 variable using char(=1 byte) pointer
   char *p2 = (char*)&memory2; //Point the starting address of the memory2 variable using char(=1 byte) pointer
   for (j = 0; j < DEFAULT_CACHE_BLOCK_SIZE_BYTE / 2; j++) {
      pEntry->data[j] = *(p + j);
      //*p means first byte of variable memory1, *(p+1) means second byte of memory1...etc
      //copy the memory1 variable(=memory_array[word_index]) each 1 byte into data[0~3]
   }

   for (j = DEFAULT_CACHE_BLOCK_SIZE_BYTE / 2; j < DEFAULT_CACHE_BLOCK_SIZE_BYTE; j++) {
      pEntry->data[j] = *(p2 + (j - 4)); //copy the memory2 variable (=memory_array[word_index+1]) each 1 byte into data[4~7]
      
   }


   /* Return the accessed data with a suitable type */
   return cache_return(pEntry, type, byte_offset);
}