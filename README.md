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
#define DEBUG 1ou0
if(DEBUG){printf}

#En C fuite de mémoire -> Valgrind

# Le remisage, git stash

Souvent, lorsque vous avez travaillé sur une partie de votre projet, les choses sont dans un état instable mais vous voulez changer de branche pour travailler momentanément sur autre chose. Le problème est que vous ne voulez pas valider un travail à moitié fait seulement pour pouvoir y revenir plus tard. La réponse à cette problématique est la commande git stash.

# Se connecter en ssh sans rentrer de mot de passe
cd .ssh
1) générer une clé ssh: ssh-keygen -t rsa
2) "Passphrase" -> faire entrer 2 fois pour pas mettre de MDP
3) id_rsa = clé privée; id_rsa.pub = clé public; copier la clé public dans un fichier "authorized_key" (tout ça dans .ssh)
4) se co à un autre ordi:
- avec un ordi de l'école -> ssh "nomdelordi"
- avec mon pc -> ssh lsteffanutto@ssh.enseirb-matmeca.fr

# ENSEIRB to MY PC
scp -r lsteffanutto at ssh enseirb-matmeca fr: <cheminDuDossier> <DestinationSurTonOrdi>

# Site de dépannage = Ohshitgit

# python librairie/package etc
https://www.youtube.com/watch?v=MxvLhp9xJo4&list=WL&index=145&t=474s


