/*
* main.c
*
* 20493-01 Computer Architecture
* Term Project on Implentation of Cache Mechanism
*
* Skeleton Code Prepared by Prof. HyungJune Lee
* Nov 15, 2021
*
*/
#include <stdio.h>
#include "cache_impl.h"
int num_cache_hits = 0; // number of cache hits
int num_cache_misses = 0; // number of cache misses
int num_bytes = 0; // number of bytes read total
int num_access_cycles = 0; // number of access cycles
int global_timestamp = 0; // timestamp
int retrieve_data(int addr, char data_type) {
   int value_returned = -1; /* accessed data */
   /* Invoke check_cache_data_hit() */
   value_returned = check_cache_data_hit(addr, data_type);
   // if hit, cache data will be returned. if not, -1 will be returned
   /* In case of the cache miss event, access the main memory by invoking access_memory() */
   if(value_returned == -1){ // in case of miss
       value_returned = access_memory(addr, data_type);
       // access_memory and then call cache_return and it returns cache data
   }
   return value_returned; // return value_returned to main's result
}
int main(void) {
   FILE *ifp = NULL, *ofp = NULL;
   unsigned long int access_addr; /* byte address (located at 1st column) in "access_input.txt" */
   char access_type; /* 'b'(byte), 'h'(halfword), or 'w'(word) (located at 2nd column) in "access_input.txt" */
   int accessed_data; /* This is the data that you want to retrieve first from cache, and then from memory */
  
   init_memory_content(); // initiate memory array
   init_cache_content(); // initiate cache array
  
   // open input file, if error, exit
   ifp = fopen("access_input.txt", "r");
   if (ifp == NULL) {
       printf("Can't open input file\n");
       return -1;
   }
  
   // open output file, if error, exit
   ofp = fopen("access_output.txt", "w");
   if (ofp == NULL) {
       printf("Can't open output file\n");
       fclose(ifp);
       return -1;
   }
  
   /* Fill out here by invoking retrieve_data() */
   while(1){
       int ret=fscanf(ifp, "%ld %c", &access_addr, &access_type); // read input file line by line in format
       if(ret==EOF) // if no input left, break
           break;
       fprintf(ofp, "%ld\t%c\t", access_addr, access_type); // write input address and data type
       int result = retrieve_data(access_addr, access_type); // calculate address's data by retrieve_data
       fprintf(ofp, "%#x\n", result); // write address's data
   }
  
   fprintf(ofp,"-----------------------------------------\n");
  
   switch(DEFAULT_CACHE_ASSOC){
       case 1: // DEFAULT_CACHE_ASSOC == 1
           fprintf(ofp,"[Direct mapped cache performance]\n"); // direct mapped
           break;
       case 4: // (DEFAULT_CACHE_BLOCK_SIZE_BYTE*DEFAULT_CACHE_ASSOC) == (DEFAULT_CACHE_SIZE_BYTE)
           fprintf(ofp,"[Fully associative cache performance]\n"); // fully associative
           break;
       default: // others, n-way set associative
           fprintf(ofp,"[%d-way set associative cache performance]\n", DEFAULT_CACHE_ASSOC);
   }
  
   float hit_ratio = (float)num_cache_hits/(num_cache_misses+num_cache_hits); // hit ratio = hit / number of access
   num_access_cycles = (num_cache_misses*(MEMORY_ACCESS_CYCLE+1)) + num_cache_hits; // acces cycles = 101 * miss + 1 * hit
   float bandwidth = (float)num_bytes/num_access_cycles; // bandwidth = number of bytes / number of access cycles
  
   // write hit ratio and bandwidth
   fprintf(ofp, "Hit ratio = %.2f (%d/%d)\n", hit_ratio, num_cache_hits, num_cache_misses+num_cache_hits);
   fprintf(ofp, "Bandwidth = %.2f (%d/%d)\n", bandwidth, num_bytes, num_access_cycles);
  
   // close input and output file
   fclose(ifp);
   fclose(ofp);
  
   // print last cache array
   print_cache_entries();
   return 0;
}
