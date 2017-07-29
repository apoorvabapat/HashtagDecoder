wordlist = open("bigwordlist1.txt");
input= open("hashtag-train.txt");
output= open ("output.txt","w");
dict={};
line=wordlist.readline();
count=0;
while (count!=75000):
    line1=line.split();
    dict[line1[0]]=line1[1];
    line=wordlist.readline();
    count+=1;
    
for line in input.readlines():
    hashtag=line;
    start=1;
    best='';
    answer='';
    end=len(hashtag);
    while(end>=start):
            sub=hashtag[start:end];
            if(sub in dict):
                if(answer==''):
                    answer=sub;
                    start=end;
                    end=len(hashtag)
                else:
                    answer=answer+' '+sub;
                    start=end;
                    end=len(hashtag);       
            else:
                if(len(sub)==1):
                    if(sub=="\n"):
                        break
                    if(answer==''):
                        answer=sub;
                        start=end;
                        end=len(hashtag)
                    else:
                        answer=answer+' '+sub;
                        start=end;
                        end=len(hashtag);
                        continue;
                    
                end=end-1;
    
    output.write(answer+"\n");
    
    
# WER:
def substCost(source,target):
    if(source==target):
        return 0;
    else:
        return 1;

def  minEditDist(target, source):
    ''' Computes the min edit distance from target to source. Figure 3.25 in the book. Assume that
    insertions, deletions and (actual) substitutions all cost 1 for this HW. Note the indexes are a
    little different from the text. There we are assuming the source and target indexing starts a 1.
    Here we are using 0-based indexing.'''
    
    n = len(target)
    m = len(source)

    distance = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        distance[i][0] = distance[i-1][0] + 1;

    for j in range(1,m+1):
        distance[0][j] = distance[0][j-1] + 1;


    for i in range(1,n+1):
        
        for j in range(1,m+1):
            distance[i][j] = min(distance[i-1][j]+1,
                                 distance[i][j-1]+1,
                                 distance[i-1][j-1]+substCost(source[j-1],target[i-1]));
                               
    return distance[n][m]/len(target);

list=[];
list1=[]
list2=[]
i=0;
input1= open("reference_answers1.txt");
input2= open("output.txt");

for i in input1:
    list1.append(i);

for i in input2:
    list2.append(i);

sum=0.0;
for i in range(0,len(list1)):
    dist=minEditDist(list1[i].split(), list2[i].split())
    sum=sum+dist;
    list.append(dist)
avg=sum/len(list1);
print(avg)



#Optimized maxmatch:

wordlist = open("bigwordlist1.txt");
input= open("hashtag-train.txt");
output= open ("output.txt","w");
dict={};
line=wordlist.readline();
count=0;
while (count!=66000):
    line1=line.split();
    dict[line1[0]]=line1[1];
    line=wordlist.readline();
    count+=1;
      

def optimize(first,second):
    
    combo=first+second;
    if(combo in dict):
        first=second=combo;
        return [first,second];
    else:
        count=1
        for i in range(0,2):
            tmp1=first[0:(len(first)-(i+1))];
            tmp2=first[-(i+1):]+second;
            count+=1;
            if(tmp1 in dict and tmp2 in dict):
                first=tmp1;
                second=tmp2; 
    return [first,second];





for line in input.readlines():
    hashtag=line;
    start=1;
    best='';
    answer='';
    end=len(hashtag);
    while(end>=start):
            sub=hashtag[start:end];
            if(sub in dict):
                if(answer==''):
                    answer=sub;
                    start=end;
                    end=len(hashtag)
                else:
                    answer=answer+' '+sub;
                    start=end;
                    end=len(hashtag);       
            else:
                if(len(sub)==1):
                    if(sub=="\n"):
                        break
                    if(answer==''):
                        answer=sub;
                        start=end;
                        end=len(hashtag)
                    else:
                        answer=answer+' '+sub;
                        start=end;
                        end=len(hashtag);
                        continue;
                    
                end=end-1;
    new_answer=[];
    result=[];
    answer1=answer.split();
    if(len(answer1)==1):
        output.write(' '.join(answer1)+"\n");
    else:
        for i in range(0,len(answer1)-1):
            result=optimize(answer1[i],answer1[i+1])
            if(i==len(answer1)-2):
                if(result[0]not in new_answer):
                    if(result[0]==result[1]):
                        new_answer=new_answer+[result[0]];
                    else:
                        new_answer=new_answer+[result[0]];
                        new_answer=new_answer+[result[1]];
                else:
                    new_answer=new_answer+[result[1]];
            else:
                new_answer=new_answer+[result[0]];
            
            answer1[i+1]=result[1];
        
        output.write(' '.join(new_answer)+"\n");
 