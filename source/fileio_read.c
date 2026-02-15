/* read from file */
FILE* fptr = fopen("file.txt", "w");
fptr = fopen("file.txt", "r");

char buffer[64] = "";
while(fscanf(fptr, "%s", buffer) == 1) {
    printf("%s ", buffer);
}
