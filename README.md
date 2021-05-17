# Quoi ?
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



- Configurer Git la première fois:
git config --global user.name "Lucas Steffanutto" (--golbal configure pour tous les projet)
git config --global user.email lucasste33@gmail.com
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto
git config --global core.editor vim
git config --global merge.tool vimdiff

- Initialisation du projet:
créer un repo sur GitHub
méthode 1:
créer un dossier local dans lequel se situera le projet
se déplacer dans ce dossier avec la console puis "git init"
méthode 2:
cloner le projet dans le dossier local où l'on souhaite le mettre

- Relier le projet au dépôt distant:
git remote add origin https://github.com/lsteffanutto/GitFlow.git (Si pas cloné le dépôt existant et qu'on veut le connecter à notre dépôt sur un serveur distant)
git branch -M main (= git --move la branch sur le master/main)
git push -u origin main (-u = all)
git push <REMOTENAME> <BRANCHNAME>

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
# git cmd
 git --version
 git log = etat du commit
 git revert = historique des commits
 git status = informations sur les fichiers modifiés et sur l'état de leur commit et de ce qui a pas été poussé


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
python -V = voir ta version de Python
Executer code python dans atom: telecharger le package " script "
Puis quand t'as écris ton code tu fais ctrl+maj+B pour l'éxécuter

Tu cherches ta LIBRAIRIES [aca](https://pypi.org/)
t'ouvres le terminal (SUR WINDOW) en mode administrateur et tu fais: pip install NOM_LIBRAIRIE

[tuto avec autres commandes pip](https://www.youtube.com/watch?v=MxvLhp9xJo4&list=WL&index=145&t=474s)

- pip = donne toutes les commandes possibles avec (pip --version)
- python -m pip install --upgrade
- pip install nomdupaquet = install ta librairie (pip uninstall nomdupaquet)
- pip search nomdupaquet = chercher un paquet
- pip show nomdupaquet = voir ses infos
- pip freeze = voir tous les paquets que t'as installé
- installer librairies quand t'as des problèmes de connexion avec le proxy: pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>
- SINON, [problème de proxy à l'agence](https://stackoverflow.com/questions/56628194/sslerror-installing-with-pip)
- Problèmes de time out: pip --default-timeout=1000 install pandas

# Anaconda
- QUAND ON UTILISE ANACONDA ON UTILISE LA COMMANDE " CONDA " et pas pip
- Problème de fenêtre trop grosse de Anaonda Navigator: go to "C:\Users\steffanutto\AppData\Roaming\.anaconda\navigator\.anaconda\navigator" ; update => enable_high_dpi_scaling = False ; restart anaconda-navigator
- Voir installation dans fichier .txt
- ouvrir les environnement avec PycharmPro, gratuit pour les étudiants
- normalement, à partir de cmd.exe de Anaconda " conda create --prefix ./path_que_tu_veux python=version_de_python (si tu fais ça en spécifiant un chemin faudra tjrs le spécifier et il aura pas de nom)
- Avec path = " C:\Users\steffanutto\Desktop\Unity_projects\kart-microgame " dans le cas Unity x Python x TensorFlow
- Montre les environnements crés: " conda info --envs "
- activer ton environnement: " conda activate C:\Users\steffanutto\Desktop\Unity_projects\kart-microgame "
- [créer différents environnements](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
- Manage environnements <3: [Tuto environment](https://towardsdatascience.com/manage-your-python-virtual-environment-with-conda-a0d2934d5195#:~:text=You%20can%20always%20use%20conda,use%20by%20using%20conda%20activate%20.&text=conda%20deactivate%20will%20deactivate%20your,which%20is%20the%20base%20environment)

# Python
- Utiliser Pycharm avec un terminal powershell
- Utiliser "Constant Design pattern" pour coder
- [Utiliser "Décorators Functions" pour pas créer des fonctions similaires et wrapper des fonctions: " @prepare pizza "](https://openclassrooms.com/en/courses/6900866-write-maintainable-python-code/7009163-create-flexible-functions-with-the-decorator-design-pattern)
- [SOLID principle](https://openclassrooms.com/en/courses/6900866-write-maintainable-python-code/7009965-discover-good-programming-practices-with-the-solid-principles)
- Créer  un fichier .gitignore pour spécifier les fichiers  qu'on veut pas ajouter un git (exemple: "envs/")
- Ajouter à un fichier "requirements.txt" toutes les bibliothèques utilisées dans un projet, faire dans le PowerShell Anaconda: "pip list > requirements.txt"
- Problemes d'indentation car  tabs se confond avec space, faire ça dans le terminal de Pycharm: python -m tabnanny src/main.py
- Re-auto indent tout le code PyCharm = Ctrl+Alt+L
- Ctrl+Alt+S = ouvrir les settings (puis go keymap pour shortcut)

- [DataSciences et Tuto Python bien](https://openclassrooms.com/en/courses/4425111-perfectionnez-vous-en-python/) voir  Chapitre 2
- [Tuto complet apprendre Python bien](https://openclassrooms.com/en/courses/6900856-learn-programming-with-python/6992862-get-the-most-out-of-this-course)
