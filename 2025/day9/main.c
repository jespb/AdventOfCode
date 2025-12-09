#include <stdio.h>
#include <stdlib.h>

int allowed(int points[1000][2], int n, int y, int x){
	int valid[] = {0,0,0,0};
	for (int i = 0; i <n; i++){
		int py = points[i][0];
		int px = points[i][1];

		if (py>=y && px>=x)
			valid[0] = 1;
		if (py>=y && px<=x)
			valid[1] = 1;
		if (py<=y && px>=x)
			valid[2] = 1;
		if (py<=y && px<=x)
			valid[3] = 1;
		if (valid[0]+valid[1]+valid[2]+valid[3] == 4){
			return 1;
		}
	}
	return 0;
}



int main(void) {
    FILE *fp = fopen("input2.txt", "r");

    int a, b;
    char line[256];

    int n = 496;
    int points[1000][2];
    for(int i = 0; i<n ;i++){
    	points[i][0]=0;
    	points[i][1]=0;
    }

    int i = 0;

    while (fgets(line, sizeof(line), fp)) {
        sscanf(line, "%d,%d", &a, &b);
        points[i][0] = a;
        points[i][1] = b;
        printf("%d,%d\n",a,b);
        i++;
    }
  
    fclose(fp);

    int max = 0;
    for (int i1 = 0; i1<n; i1++){
    	int y1 = points[i1][0];
    	int x1 = points[i1][1];

    	for (int i2 = 0; i2<i1; i2++){
    		int y2 = points[i2][0];
    		int x2 = points[i2][1];
    		//printf("comparing (%d, %d) - (%d, %d)\n",y1,x1,y2,x2);
    		int valid = 1;

    		int yii = y1<y2?y1:y2;
    		int xii = x1<x2?x1:x2;
    		int yia = y1>y2?y1:y2;
    		int xia = x1>x2?x1:x2;
    		int yi = yii;
    		while (valid && yi<yia){
	    		int xi = xii;
	    		while (valid && xi<xia){
	    			if (allowed(points, n, yi, xi) == 0)
    					valid = 0;
    				xi++;
    			}
    			yi ++;
    		}
    		if (valid==1){
    			int d = (abs(y2-y1)+1)*(abs(x2-x1)+1);
    			if (d > max){
    				max = d;
    				printf("%d\n",max);
    			}
    		}

    	}

    }


    return 0;
}

