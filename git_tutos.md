# Git
- Git = gestionnaire de version ; GitHub = service en ligne qui héberge les dépôts Git. On parle alors de dépôt distant
- Dépôt local = enregistre les versions de ton code pour pouvoir y accéder si besoin (les versions y sont stockées au fur et à mesure)
=> Copie du dépôt distant, permettant d'ajouter des modifications.
- Dépôt distant = stocke les différentes versions du code pour avoir un historique délocalisé hébergé sur Internet
- branche = copie du code principal à un instant T
- Git Bash = Utiliser Git en ligne de commande
- Working Directory = dossier du projet sur l'ordinateur "Expert_Git"
- Stage/index = zone intermédiaire entre working directory et repository = tous les fichiers modifiés qu'on veut voir apparaître dans la prochaine version de code
- Repository = Quand on crée une nouvelle version d'un projet c'est dans cette zone qu'elle est stockée.
- Repository GitHub = dépôt distant

Stage/index:
=> Quand on créer un fichier on doit l'indexer: "git add index.html" => il passe alors dans l'index/stage
=> Quand on a modifié ce fichier il faut refaire un git add pour prendre en compte les modifications
=> Soit git add nomdufichier, soit git add -A (tous les fichiers)

Repository:
=> git commit créer une nouvele version du projet, et passe les fichiers qui sont dans le stage, dans le Repository: " git commit -m "description du commit" "
=> nouvelle version du projet sur branch master


- git pull à partir d'une branch march pas car il y a des conflits: 
=> git stash (sauvegarde ce que t'as dans une petite boîte)
=> git drop (tu le balance)
=> git pull 
(=> git stash pop remet ce que t'avais fait par dessus ? !!! problèmes de merge après)

- SINON !!! OUI !!!
=> git fetch + git checkout

- Linux double click selectionne tout dans le terminal puis molette copie direct sur la line de commande 

- git checkout recupere dans ton working directory, ce qu'il y a dans ta database, directory .git, remet même état que le dernier commit

- git diff nom du fichier

- git commit --amend, prend le dernier commit et le rajoute 

- git reset = degage ce qu'il y a dans le git add .

- Configurer Git la première fois:
git config --list --show-origin (voir les bails)
git config --global user.name "Lucas Steffanutto" (--golbal configure pour tous les projet)
git config --global user.email lucasste33@gmail.com
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto
git config --global core.editor vim
git config --global merge.tool vimdiff
[PROXY](https://stackoverflow.com/questions/783811/getting-git-to-work-with-a-proxy-server-fails-with-request-timed-out): git config --global http.proxy http://LucasAdmin:lucasadmin@proxy-1.ims.bordeaux:3128

- Initialisation du projet:
créer un repo sur GitHub
    - méthode 1:
créer un dossier local dans lequel se situera le projet
se déplacer dans ce dossier avec la console puis "git init"
    - méthode 2:
cloner le projet dans le dossier local où l'on souhaite le mettre

- Relier le projet au dépôt distant:
    - faire les git config ci-dessus si première fois
    - git init
    - git remote add origin https://github.com/lsteffanutto/GitFlow.git (Si pas cloné le dépôt existant et qu'on veut le connecter à notre dépôt sur un serveur distant)
    - git branch -M main (= git --move la branch sur le master/main)
    - git add .
    - git commit -m "ouais"
    - git push -u origin main (-u = all)
    - git push <REMOTENAME> <BRANCHNAME>

!!!Depuis Oactobre 2020 on appelle la branch pincipale "main"!!!

- Accéder à un dépôt distant et le copier en local
git init
git remote add _nomcourt_ https://github.com/lsteffanutto/GitFlow.git (pour que le dépôt pointe sur le dépôt distant)
git branch -M main
git pull _nomcourt_ main (récupérer et fusionner les modifications d'un remote repository sur la branch actuelle (fusionne fetch+merge ?) )
=> premier commit avec vim: 
- Type i . The editor opens in 'normal' mode, where everything you type is interpreted as a command and where you can do stuff like saving the file and exiting. ...
- Write your commit message on the first line.
- Hit esc . This will return you to 'normal' mode.
- Type :wq to leave
- 

## git token
- Générer le token et l'ajouter à windows: [ici](https://stackoverflow.com/questions/68775869/support-for-password-authentication-was-removed-please-use-a-personal-access-to)
- Essayer de push 
``` 
git push -u origin main
``` 
- Si ça marche pas ET DEJA GENERER TOKEN FAIRE ça (avec le token généré), remplacer l'origin et refaire le push précédent et c'est bon
``` 
git remote show origin
git remote remove origin (ICI DIRECT)
git remote show origin
git remote add origin https://personal_token@github.com/git_username/repo_a_relier.git (ICI DIRECT)
git remote show origin
git push -u origin main
``` 
    
git a project whene yet a .git in a subfolder => delete .git in the subfolder 
    
## git cmd
git --version
git log = etat du commit
git revert = historique des commits
git status = informations sur les fichiers modifiés et sur l'état de leur commit et de ce qui a pas été poussé


## how to commit
 
git init
git clone "nom du repository"

push un msg
git add -A
git commit -m "message"
git push

## how to tirer du code en forçant

git reset --hard HEAD
git pull
(annule mes modifs puis pull)

pour concatener les deux versions
git pull sur mon pc 
gerer les conflits sur atom
puis les repush sur git hub

## créer une branche
git checkout -b nomdelabranche = créer une branche;
git branche -> vérifie sur quelle branche t'es;
git diff -> voir les baux;

#Push to a Branch
If your local branch does not exist on the remote, run either of these commands:
git push -u origin my-branch-name;
If your local branch already exists on the remote, run this command: git push;

#Puis pour récup sur un autre PC
git pull
git checkout nombranche (qui est caché)

#Merge une branch
Bien vérifier la branch et faire un push sur la branch
tu te mets sur la branch master (git checkout master)
puis tu fais git merge "nomdelabrancheàavaler" (pour envoyer ta branch sur le master)
PUIS 
git push pour l'envoyer sur git

#.gitignore => permet de mettre dans fichier .txt les paths correspondant aux fichier qu'on ne veut pas ajouter
- enlever un truc déjà dans ton commit: " git rm -r --cached PATH_du_truc_a_enlever " (cela ne supprime pas le fichier)
- sinon t'enleve tout, tu mets à jour le git ignore et tu recommit "git rm -r --cached ."; "git add ." ; git commit -m "gitignore fix";
!!! attention sur gitbash "path1/path2", si tu copie les chemins windows c'est "path1\path2" donc GitBash "chemin introuvable"
# Graph des branchs
git log --oneline --graph

[méga schéma](https://www.sebastien-gandossi.fr/blog/difference-entre-git-reset-et-git-rm-cached)

# Voir la racine d'un projet
git rev-parse --show-toplevel
 
# Annuler un commit (puis refaire add, commit push)
git reset --soft HEAD~1

# Voir le repo
tig

# Enlever et mettre tout les printf 
#define DEBUG_SERVER (0 ou 1)
if(DEBUG_SERVER) printf("");
#define DEBUG 1ou0
if(DEBUG){printf}

#En C fuite de mémoire -> Valgrind

# Le remisage, git stash

Souvent, lorsque vous avez travaillé sur une partie de votre projet, les choses sont dans un état instable mais vous voulez changer de branche pour travailler momentanément sur autre chose. Le problème est que vous ne voulez pas valider un travail à moitié fait seulement pour pouvoir y revenir plus tard. La réponse à cette problématique est la commande git stash.

# Untrack big file of your repository
- En local, on peut se mettre à l'emplacement du .git de notre projet et lancer la commande " **du -sh .git** " : pour voir l'usage disque du repository.
- En local, pour voir le détail en utilisant Git lui même, en lançant la commande : " **git count-objects -vH** "
- En local, pour voir la taille de nos propre repository git ici : [settings/repositories](https://github.com/settings/repositories)
- En local avec git, pour voir les **10 fichiers les plus volumineux du repo**, utiliser la commande :
  ``` 
  git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | sed -n 's/^blob //p' | sort --numeric-sort --key=2 | tail -n 20 | cut -c 1-12,41-
  ```
- En local, pour voir la **taille des fichiers les plus lourd de mon repo .git**, utiliser la commande :
  ```
  git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  sed -n 's/^blob //p' |
  sort --numeric-sort --key=2 |
  cut -c 1-12,41- |
  $(command -v gnumfmt || echo numfmt) --field=2 --to=iec-i --suffix=B --padding=7 --round=nearest
```
- En local, les fichiers trackés par git classé par ordre décroissant de taille en MB:
```
git ls-tree -r HEAD --long | awk '{print int($4/1024)"\t"$5}' | sort -k 1 -nr | awk '{print int($1/1024)" MB\t"$2}'
```
  
- 1. Penser à **mettre à jour le .gitignore** pour ne pas tracker les fichier volumineux, en ajoutant par exemple les lignes :
  ```
  /data/online/*.csv
  /data/res/
  ```
- 2. Pour dire à Git de **untrack certains fichiers ou repositories**, exécuter la commande
  ```
  git rm --cached FILE_OR_DIRECTORY_NAME
  ```
  **Note** : Pour faire la **liste de tous les fichiers commençant par le même path ou prefix**, on peut utiliser la commande :
  ```
  git ls-files | grep '^prefix'
  ```
  Pour **untrack la liste de tous ces fichiers**, utiliser la commande :
  ```
  git ls-files | grep '^prefix' | xargs git rm --cached
  ```
  Pour **untrack tous les fichiers avec un certains format** (ici ".html" par exemple), recurssivement dans tous les dossiers du repo, utiliser la commande :
  ```
  git rm --cached -r *.html
  ```

  **Note**: Avec le **.gitignore, pour untrack tous les fichiers avec un certains format, à l'exceptions de certains** que l'on veut push
  ```
  # Ignore all HTML files
  *.html
  # But do not ignore these specific HTML files
  !important-file.html
  !folder/subfolder/another-important-file.html
 ```

- 3. On peut vérifier la manipulation avec git status puis ensuite refaire git add . et git commit et git push


