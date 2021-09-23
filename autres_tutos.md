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
