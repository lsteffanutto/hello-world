# git cmd
 
 git log = etat du commit
 git revert = historique des commits
 git status = infos de ce qui a pas été poussé
 
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

# créer une branche
git checkout -b nomdelabranche -> créer une branche
git branche -> vérifie sur quelle branche t'es
git diff -> voir les baux

Puis pour récup sur un autre PC
git pull
git checkout nombranche (qui est caché)

#Merge une branch
Bien vérifier la branch et faire un push sur la branch
tu te mets sur la branch master (git checkout master)
puis tu fais git merge "nomdelabrancheàavaler" (pour envoyer ta branch sur le master)
PUIS 
git push pour l'envoyer sur git

# Enlever et mettre tout les printf 
#define DEBUG_SERVER (0 ou 1)
if(DEBUG_SERVER) printf("");
