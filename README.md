# git cmd
 git --version
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

# Anaconda
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
