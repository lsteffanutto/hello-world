# faire une branche
git branch -b lenomdelabranche
quand la branche marche et ajout fonctionnalité
git push origin master
(top = faire branch master avec zero problem puis en parallèle une branch de dev principale pour fixer petit bug avant de faire un mega push sur la branche master)

# git cmd
 
 git log = etat du commit
 git revert historique des commits
 
 # how to commit
 
 git init
 git clone "nom du repository"
 
 push un msg
 git add -A
 git commit -m "message"
 git push
 
 # how to tirer du code en forçant
 
 git reset --hard HEAD
 git pull
 (annule mes modifs puis pull)
 
 pour concatener les deux versions
 git pull sur mon pc 
gerer les conflits sur atom
puis les repush sur git hub
