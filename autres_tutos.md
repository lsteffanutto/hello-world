# Proxy
- pip install --proxy=http://192.168.251.1:3128 -r requirements3.txt
- Time error proxy block notebook download from an url
``` 
import os
os.environ['http_proxy'] = "http://LucasAdmin:lucasadmin@proxy-1.ims.bordeaux:3128" 
os.environ['https_proxy'] = "https://LucasAdmin:lucasadmin@proxy-1.ims.bordeaux:3128"
```
La mettre au bon endroit de la requete url et de la connexion (resnet.py)

# Alias_Doskeys
- ALIAS BASH: " alias nom_de_votre_alias="commande de votre alias" ; les ajouter dans le bashrc
- ALIAS WIN: " doskey macroName=macroDefinition " 
- Permanent, depuis une console window (que la console aura quand elle demarre):
- créer un fichier .txt qu'on nomme macros.doskey et le stocker où on veut
- ajouter les raccourcis souhaités sur chaque ligne, exemples: "ls=dir $* $T", "ci=conda info --envs $T" etc
- " reg add "HKCU\Software\Microsoft\Command Processor" /v Autorun /d "doskey /macrofile=\"C:\PATH_JUSQUA\macros.doskey.txt"" /f "  (ajoute le fichier au registre "opération effectué")
- " reg query "HKCU\Software\Microsoft\Command Processor" /v Autorun " doit retourner le bon chemin (" Autorun    REG_SZ    doskey /macrofile="C:\PATH_JUSQUA\macros.doskey.txt"). Fermer la console, la reouvrir et c'est bon

# Anaconda
- conda env remove -n ENV_NAME
- QUAND ON UTILISE ANACONDA ON UTILISE LA COMMANDE " CONDA " et pas pip
- Problème de fenêtre trop grosse de Anaonda Navigator: go to "C:\Users\steffanutto\AppData\Roaming\.anaconda\navigator\.anaconda\navigator" ; update => enable_high_dpi_scaling = False ; restart anaconda-navigator
- Voir installation dans fichier .txt
- ouvrir les environnement avec PycharmPro, gratuit pour les étudiants
- normalement, à partir de cmd.exe de Anaconda " conda create --name my_env python=3.7  "
- Montre les environnements crés: " conda info --envs "
- activer ton environnement: " conda activate my_env "
- [créer différents environnements](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
- Manage environnements <3: [Tuto environment](https://towardsdatascience.com/manage-your-python-virtual-environment-with-conda-a0d2934d5195#:~:text=You%20can%20always%20use%20conda,use%20by%20using%20conda%20activate%20.&text=conda%20deactivate%20will%20deactivate%20your,which%20is%20the%20base%20environment)

- Probleme de build "Microsoft Visual C++ 14.0 or greater is required":
    - télécharger ça https://visualstudio.microsoft.com/fr/visual-cpp-build-tools/
    - télécharger Visual Studio Build Tools 2019 
    - mettre à jour Visual Studio, et cliquer sur “Modifier”
    - Choisir “ composants individuels “
    - Ajouter “Ensemble d’outils VC++ 2015.3 v14.00 (v140) ”
    - Sinon peut être:
    - conda install -c conda-forge implicit
    - pip install --proxy=http://192.168.251.1:3128 gevent --pre
    - pip install --proxy=http://192.168.251.1:3128 auto-py-to-exe

- OMP Error (noyau notebook plante): 
``` 
#OMP Error:
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
```

- “ RuntimeError: Attempting to deserialize object on a CUDA device but torch.cuda.is_available() is False.”: installer une version stable de PyTorch
``` 
pip uninstall torch
pip cache purge
pip install --proxy=http://192.168.251.1:3128 torch -f https://download.pytorch.org/whl/torch_stable.html
```

error OpenCV: The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support
``` 
pip uninstall opencv-python 
pip install opencv-python
```

Dans un projet our importer les fonctions d'autres dossier, il faut ajouter le path python du projet, sinon erreur du type
"""    from models.resnet import rf_lw50, rf_lw101, rf_lw152
ModuleNotFoundError: No module named 'models' """
``` 
sys.path.append('C:/Users/Lucas/Desktop/test/light-weight-refinenet')
```

La commande " env " permet de voir les variables d'environnement

Path to a train directory for ML: if error "    fp = builtins.open(filename, "rb")
**OSError: [Errno 22] Invalid argument**: 'C:/Users/Lucas/Desktop/test/light-weight-refinenet/examples/imgs/nyu_training_dataset/train_part/train_labels/000116.png **\r** ' ""
In a script of the project, find a type of the first line and replace it with the second
```
lambda x: x.decode("utf-8").strip("\n").split("\t"), datalist   # ===> original, developed on unix
lambda x: x.decode("utf-8").strip("\r\n").split("\t"), datalist # ===> actual, developed on windows ("error")
```
In Jupyter Notebook to import function form an other file, install the following package and write the following import where you want
```
pip install ipynb
from ipynb.fs.full.main import *
```

To get all the PyTorch/CUDA/cuDNN/GPU infos : ``` python -m torch.utils.collect_env ```


Quand imshow() OpenCV => pas le bon path de l'image 

torch to numpy (opencv):
```
output.cpu().data.numpy().argmax()
output.cpu().detach().numpy()
output.cpu().detach().squeeze().numpy()
reverse = torch.from_numpy(tensor)
```
tqdm() permet d'afficher une "loading" bar durant computing
```
for i, sample in enumerate(tqdm(val_loader)):
```

# Variables d'environnement et Java
- check JAVA_HOME : " echo %JAVA_HOME%
- check version de java et openJDK : " java --version " et " javac --version "
- Si JAVA_HOME ne pointe pas vers le jdk, modifier cette variables d'env : C:\Program Files\Java\jdk-17.0.2
- Reboot le pc pour que les variables d'environnements se mettent à jour

# Variables d'environnement et Java
- 401 is authentication error : user:password
- 403 is authorization error : certificates

# SSH
## Se connecter en ssh sans rentrer de mot de passe
cd .ssh
1) générer une clé ssh: ssh-keygen -t rsa
2) "Passphrase" -> faire entrer 2 fois pour pas mettre de MDP
3) id_rsa = clé privée; id_rsa.pub = clé public; copier la clé public dans un fichier "authorized_key" (tout ça dans .ssh)
4) se co à un autre ordi:
- avec un ordi de l'école -> ssh "nomdelordi"
- avec mon pc -> ssh lsteffanutto@ssh.enseirb-matmeca.fr

## ENSEIRB to MY PC
scp -r lsteffanutto at ssh enseirb-matmeca fr: <cheminDuDossier> <DestinationSurTonOrdi>
    
## Virus vst
https://veryleaks.cz/threads/vstcrack-trojan-nettoyage-pc-infecte-par-un-vst-de-vstcrack-com.191218/

