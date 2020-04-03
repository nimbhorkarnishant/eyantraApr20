# WorkFlow

## Dont work directly on master branch
step1 : create a branch for a feature you want to work on <br>
$ git branch print-uni # 1.created branch, print-uni <br>
$ git branch # check if branch created <br>
 * master # * means - current branch<br>
   print-uni<br>
$ git checkout print-uni # 2.switch to that print-uni branch<br>

step2 : <br>
#inside print-uni branch<br>
1.make changes to anyfile you want all over djangowebsite<br>
2.$ git add -A<br>
3.$ git commit -m 'joey' #add messages properly<br>
it has no effect on remote repo yet.<br>
#add messages using vim<br>
3.$ git commit <br>
opens vim <br>
write msg
press i
press Esc
press :wq
#add msgs using nano
3.$ git commit 
write msg
ctrl + x
y
press enter


step3 : 
#change remote repo
$ git push -u origin print-uni

step4 :
#1. switch to master
$ git checkout master
#2. check if changes to (origin master) made by someone else (remote one)
$ git pull origin master

#print-uni not yet branch of master
$ git branch  #branches we have merged so far
*master
#3. merge print-uni (to master)
$ git merge print-uni
#git branch --merged
*master
print-uni

#4. push change to origin(remote repo)
$ git push origin master

step5 :

once you have merged a branch to the master you can delete it
#1. delete locally
$ git branch -d print-uni
#2. delete from remote repo
$ git push origin --delete print-uni

