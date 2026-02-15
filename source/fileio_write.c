/* write to file */
FILE* fptr = fopen("file.txt", "w");
fprintf(fptr, "hello world");
fclose(fptr);
