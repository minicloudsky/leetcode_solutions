#include <stdio.h>
#include <stdlib.h>
typedef struct LinkedList
{
	int no;
	struct LinkedList* next;
}LinkedList;

LinkedList *Link()
{
	LinkedList* head=NULL;
	LinkedList *p;
	int  flag;
	while(1)
	{
		printf("ÊÇ·ñÌí¼ÓÔªËØ1/0:");
		scanf("%d",&flag);
		if(flag==0)
			break;
		if(head==NULL)
		{
			if((head=(LinkedList *)malloc(sizeof(LinkedList)))==NULL)
				exit(0);
			printf("ÇëÊäÈëno:");
			scanf("%d",&head->no);
			head->next=NULL;
			continue;
		}
		if((p=(LinkedList *)malloc(sizeof(LinkedList)))==NULL)
			exit(0);
		printf("ÇëÊäÈëno:");
		scanf("%d",&p->no);
		p->next=head->next;
		head->next=p;
	}
	return head;
}

void print(LinkedList* head)
{
	LinkedList *p=head;
	while(p->next!=NULL)
	{
		printf("%d  ",p->no);
		p=p->next;
	}
	printf("%d",p->no);
	puts("");
}

int main()
{
	int n;
	LinkedList* head;
	head=Link();
	print(head);
	return 0;
}
