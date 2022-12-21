#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include <stdlib.h>
#define MAX 31
#define DATE 11
#define FEE_PAID 4
#define NAME 25
#define ORGANIZATION 35
#define JOB 15

struct ARRAY {
    int tag;
    char date[DATE];
    char fee_paid[FEE_PAID];
    char name[NAME];
    int age;
    char organization[ORGANIZATION];
    char job[JOB];
};

struct NODE {
    int tag;
    char date[DATE];
    char fee_paid[FEE_PAID];
    char name[NAME];
    int age;
    char organization[ORGANIZATION];
    char job[JOB];
    struct NODE* next;
};

struct NODE* createNewNode(int tag, char date[DATE], char fee_paid[FEE_PAID], char name[NAME], int age, char organization[ORGANIZATION], char job[JOB]) {
    struct NODE* temp2 = (struct NODE*)malloc(sizeof(struct NODE)); // memory allocation
    temp2->tag = tag;
    strcpy(temp2->date, date);
    strcpy(temp2->fee_paid, fee_paid);
    strcpy(temp2->name, name);
    temp2->age = age;
    strcpy(temp2->organization, organization);
    strcpy(temp2->job, job);
    temp2->next = NULL;
    return temp2;
}

void linkNode(struct NODE* head, struct NODE* node) {
    /*  linkeNode head->next = node  */
    struct NODE* cNode = head;
    struct NODE* pNode = NULL;
    while (cNode != NULL) {
        pNode = cNode;
        cNode = cNode->next;
    }
    node->next = cNode;
    pNode->next = node;
}

void swap(struct ARRAY* a, struct ARRAY* b) {
    /*  swap a and b  */
    struct ARRAY tmp = *a;
    *a = *b;
    *b = tmp;
}

void print_struct_array(struct ARRAY* temp1, int count) {
    /*  print struct array with space  */
    struct ARRAY* ptr = temp1;
    printf("%d %s %s %s %d %s %s\n",
        ptr[count].tag, ptr[count].date, ptr[count].fee_paid, ptr[count].name,
        ptr[count].age, ptr[count].organization, ptr[count].job);
}

void print_linked_list(struct NODE* temp2) {
    /*  print the linked-list  */
    struct NODE* ptr = temp2;
    printf("%d %s %s %s %d %s %s\n",
        ptr->tag, ptr->date, ptr->fee_paid, ptr->name,
        ptr->age, ptr->organization, ptr->job);

}

/* This part is main fuction of program  */
void setup(struct ARRAY* temp1, struct NODE* temp2, int* num, const char* name) {
    /*  Read file and store in struct array and linked-list  */
    struct NODE* head = NULL;
    struct NODE* tmp;
    FILE* myInFile;
    myInFile = fopen(name, "r");
    if (myInFile == NULL)
        printf("Could not open %s!\n", name);
    int count = 0;
    char line[200];
    while (fgets(line, sizeof(line), myInFile) != NULL) {
        /*  get one line and  cut about "/"  */
        char* token = strtok(line, "/");
        int i = 0;
        /*  make a stuct array  */
        while (token != NULL)
        {
            if (i == 0)
                temp1[count].tag = atoi(token);
            else if (i == 1)
                strcpy(temp1[count].date, token);
            else if (i == 2)
                strcpy(temp1[count].fee_paid, token);
            else if (i == 3)
                strcpy(temp1[count].name, token);
            else if (i == 4)
                temp1[count].age = atoi(token);
            else if (i == 5) {
                strcpy(temp1[count].organization, token);
                token = strtok(NULL, "\n"); //cut of "\n"
                strcpy(temp1[count].job, token);
                break;
            }
            token = strtok(NULL, "/");
            i++;
        }
        /*  make a linked-list  */
        if (count == 0)
            head = createNewNode(temp1[count].tag, temp1[count].date, temp1[count].fee_paid, temp1[count].name, temp1[count].age, temp1[count].organization, temp1[count].job);
        else {
            tmp = createNewNode(temp1[count].tag, temp1[count].date, temp1[count].fee_paid, temp1[count].name, temp1[count].age, temp1[count].organization, temp1[count].job);
            linkNode(head, tmp);
        }
        count++;
    }
    *temp2 = *head;
    *num = count;
    fclose(myInFile);
}

void p1_1(struct ARRAY* temp1, int num) {
    /*  search the 'Choi' in struct array and print all information  */
    printf("\n[search the 'Choi' in struct array and print all information]\n");
    struct ARRAY* ptr = temp1;
    char sub[5] = "Choi";
    for (int i = 0; i < num; i++)
        if (strstr(ptr[i].name, sub) != NULL)
            print_struct_array(ptr, i);
}

void p1_2(struct NODE* temp2) {
    /*  search the 'Choi' in linked-list and print all information  */
    printf("\n[search the 'Choi' in linked-list and print all information]\n");
    struct NODE* ptr = temp2;
    char sub[5] = "Choi";
    while (ptr->next != NULL) {
        if (strstr(ptr->name, sub) != NULL)
            print_linked_list(ptr);
        ptr = ptr->next;
    }
}

void p2_1(struct ARRAY* temp1, int num) {
    /* Search for all from Gachon University in struct array */
    printf("\n[Search for all from Gachon University in struct array]\n");
    struct ARRAY* ptr = temp1;
    char sub[18] = "Gachon University";
    for (int i = 0; i < num; i++)
        if (strstr(ptr[i].organization, sub) != NULL)
            print_struct_array(ptr, i);
}

void p2_2(struct NODE* temp2) {
    /* Search for all from Gachon University in linked-list */
    printf("\n[Search for all from Gachon University in linked-list]\n");
    struct NODE* ptr = temp2;
    char sub[18] = "Gachon University";
    while (ptr != NULL) {
        if (strstr(ptr->organization, sub) != NULL)
            print_linked_list(ptr);
        ptr = ptr->next;
    }
}


void p3(struct ARRAY* head, int n) {
    /*  Sort the data in the array in tag# order   */
    printf("\nData in struct array is sorted\n");
    int i, j;
    for (i = 0; i < n - 1; i++) {
        for (j = n - 1; j > i; j--)
            if (head[j - 1].tag > head[j].tag)
                swap(&head[j - 1], &head[j]);
    }
}

void p4(struct ARRAY* temp1, struct NODE* sorted_temp, int num) {
    /*  Create a linked list using the sorted data  */
    struct NODE* head = NULL;
    struct NODE* tmp;
    for (int count = 0; count < num; count++) {
        if (count == 0)
            head = createNewNode(temp1[count].tag, temp1[count].date, temp1[count].fee_paid, temp1[count].name, temp1[count].age, temp1[count].organization, temp1[count].job);
        else {
            tmp = createNewNode(temp1[count].tag, temp1[count].date, temp1[count].fee_paid, temp1[count].name, temp1[count].age, temp1[count].organization, temp1[count].job);
            linkNode(head, tmp);
        }
    }
    *sorted_temp = *head;
}

void p5(struct NODE* sorted_temp, int num, const char* name) {
    /*  Write the sorted data to a text file  */
    struct NODE* ptr = sorted_temp;
    FILE* myOutFile;
    myOutFile = fopen(name, "w");
    printf("\nSorted data is written in 'sorted data.txt'\n");
    while (ptr != NULL) {
        fprintf(myOutFile, "%d %s %s %s %d %s %s\n", ptr->tag, ptr->date, ptr->fee_paid, ptr->name,
            ptr->age, ptr->organization, ptr->job);
        ptr = ptr->next;
    }
    fclose(myOutFile);
}

void p6_1(struct ARRAY* temp1, int* num) {
    /* All “Choi”s canceled registration in struct array */
    struct ARRAY* ptr = temp1;
    int cnt = *num;
    char del[5] = "Choi";
    printf("\n[All “Choi”s canceled registration in struct array]\n");
    for (int i = 0; i < cnt; i++) {
        if (strstr(ptr[i].name, del) != NULL) {
            for (int j = i; j < cnt; j++) {
                ptr[j + 1].tag--;
                ptr[j] = ptr[j + 1]; // overwrite it with the next data.
            }
            cnt--; i--;
        }
    }
    for (int j = 0; j < cnt; j++)
        print_struct_array(temp1, j);
    *num = cnt;
}

void p6_2(struct NODE* head) {
    /*  All “Choi”s canceled registration in linked list  */
    int t = 0, cnt = 0, cnt_first = 0;
    struct NODE* ptr = head;
    struct NODE* pNode = NULL;
    printf("\n[All “Choi”s canceled registration in linked list]\n");
    char del[5] = "Choi";
    while (ptr != NULL) {
        if (strstr(ptr->name, del) != NULL) {
            cnt++;
            if (ptr->next == NULL) {
                pNode->next = NULL;
                free(ptr); // clear the memory
                break;
            }
            else if (t == 0) {  // if find "Choi" in first node, 'head = head->next'
                cnt_first++;
                pNode = head;
                ptr = ptr->next;
            }
            else {
                t = 1;
                pNode->next = ptr->next;
                //free(ptr); // clear the memory
                ptr = ptr->next;
            }
        }
        else {
            t = 1;
            pNode = ptr;
            for (int j = 0; j < cnt; j++)
                ptr->tag--;
            ptr = ptr->next;
        }
    }
    for (int i = 0; i < cnt_first; i++) {
        *head = *head->next;
    }
    while (head != NULL) {
        print_linked_list(head);
        head = head->next;
    }
}

void p7_1(struct ARRAY* temp1, int num) {
    /*  Give Paik's tag# in consideration of the tag# of the registered persons. Add the data to the array  */
    /*  "tag#/2021-11-30/yes/Gildong Paik/35/Gachon University/Student"  */
    printf("\n[Add data in struct array at last index]\n");
    struct ARRAY* ptr = temp1;
    ptr[num].tag = num + 1;
    strcpy(ptr[num].date, "2021-11-30");
    strcpy(ptr[num].fee_paid, "yes");
    strcpy(ptr[num].name, "Gildong Paik");
    ptr[num].age = 35;
    strcpy(ptr[num].organization, "Gachon University");
    strcpy(ptr[num].job, "Student");

    /*  print added sturct array  */
    for (int j = 0; j < num + 1; j++)
        print_struct_array(ptr, j);
}

void p7_2(struct NODE* temp2, int* num) {
    /* add data in sorted linked-list at last, "tag#/2021-11-30/yes/Gildong Paik/35/Gachon University/Student"  */
    printf("\n[Add data in linked-list at last node]\n");
    struct NODE* ptr = temp2;
    struct NODE* tmp;
    char name[NAME] = "Gildong Paik";
    char date[DATE] = "2021-11-30";
    char fee_paid[FEE_PAID] = "yes";
    char organization[ORGANIZATION] = "Gachon University";
    char job[JOB] = "Student";
    while (1) {
        if (ptr->next == NULL) {
            tmp = createNewNode(*num + 1, date, fee_paid, name, 35, organization, job);
            linkNode(ptr, tmp);
            break;
        }
        ptr = ptr->next;
    }
    /*  print added linked-list  */
    while (temp2 != NULL) {
        print_linked_list(temp2);
        temp2 = temp2->next;
    }
    num++;
}

void p8_1(struct ARRAY* temp1, int num, unsigned char* org_check_sum) {
    /*  Copy the most recent data in the array then make "p8-1.txt" and checksum.  */
    struct ARRAY* ptr = temp1;
    int cnt = num;
    // last 10 data in the array write in "p8-1.txt"
    FILE* myOutFile = fopen("p8-1.txt", "w"); // original textfile.
    for (int i = cnt - 9; i <= cnt; i++) {
        fprintf(myOutFile, "%s\n", ptr[i].name);
    }
    // checksum in original textfile.
    unsigned char name = 0;
    unsigned char check_sum = { NULL };
    for (int i = cnt - 9; i <= cnt; i++) {
        for (int j = 0; j < strlen(ptr[i].name); j++) {
            if (j == 0)
                name = ptr[i].name[j];
            else
                name += ptr[i].name[j];
        }
        if (i == cnt - 9)
            check_sum = name;
        else
            check_sum ^= name;
    }
    fprintf(myOutFile, "%d\n", check_sum);
    printf("\nOriginal data checksum : %d\n", check_sum);
    fclose(myOutFile);
    *org_check_sum = check_sum;
}

void p8_2(unsigned char org_check_sum) {
    /*  Copy the "p8-1.txt" at "p8-2.txt" and check the checksum. If checksum is same, the copy is success.  */
    struct ARRAY checksum[11] = { NULL };
    char line[NAME];
    unsigned char name = 0;
    unsigned char check_sum = 0;
    /*  Read the original textfile. */
    FILE* myInFile = fopen("p8-1.txt", "r");
    for (int i = 0; i < 10; i++) {
        fgets(line, NAME, myInFile);
        strcpy(checksum[i].name, strtok(line, "\n"));
    }
    fclose(myInFile);
    /*  checksum in copy textfile.  */
    FILE* myOutFile = fopen("p8-2.txt", "w");
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < strlen(checksum[i].name); j++) {
            if (j == 0)
                name = checksum[i].name[j];
            else
                name += checksum[i].name[j];
        }
        if (i == 0)
            check_sum = name;
        else
            check_sum ^= name;
    }
    /*  write a copy textfile.  */
    for (int i = 0; i < 10; i++)
        fprintf(myOutFile, "%s\n", checksum[i].name);
    fprintf(myOutFile, "%d\n", check_sum);
    fclose(myOutFile);

    printf("\nCopy data checksum : %d\n", check_sum);
    /*  Compare the checksum against the checksum in the original data.  */
    if (org_check_sum == check_sum)
        printf("\nVerification of successful copy\n");
    else
        printf("\nFail of data copy\n");
}

void main() {
    // 파일경로 수정해야 돌아갈거임..
    
    int num; // count the array
    unsigned char org_check_sum; // check the original checksum.
    struct ARRAY temp1[MAX] = { NULL };
    struct NODE temp2;
    struct NODE sorted_temp;

    /*  Read a text file provided and store is sturct array and linked-list.  */
    setup(temp1, &temp2, &num, "registraion_data.txt");

    /*  Search for “Choi” (if found, print all information about the persons).  */
    p1_1(temp1, num); // in the struct array
    p1_2(&temp2); // in the linked-list

    /*  Search for all from Gachon University (if found, print all information about the persons).  */
    p2_1(temp1, num); // in the struct array
    p2_2(&temp2); // in the linked-list

    /*  Sort the data in the array in tag# order.  */
    p3(temp1, num);

    /*  Create a linked list using the sorted data.  */
    p4(temp1, &sorted_temp, num);

    /*  Write the sorted data to a text file that name is "sorted_data.txt"  */
    p5(&sorted_temp, num, "p5-1.txt");

    /*  All “Choi”s canceled registration. Remove the data from  */
    p6_1(temp1, &num); // in the struct array
    p6_2(&sorted_temp); // in the linked-list

    /*  One “Paik” registered late. "tag#/2021-11-30/yes/Gildong Paik/35/Gachon University/Student"  */
    /*  Give Paik's tag# in consideration of the tag# of the registered persons.  */
    p7_1(temp1, num); // in the struct array
    p7_2(&sorted_temp, &num); // in the linked-list

    /*  Exclusive OR Checksum  */
    p8_1(temp1, num, &org_check_sum);  // Copy the most recent data in the array then make "p8-1.txt" and checksum.
    p8_2(org_check_sum); // Copy the "p8-1.txt" at "p8-2.txt" and check the checksum. If checksum is same, the copy is success.
}