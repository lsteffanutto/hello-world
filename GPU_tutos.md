# Point Culture GPU
Graphic Driver: Le pilote (en anglais, driver) de la carte graphique, est avant tout un logiciel qui s'intercale entre le système d'exploitation et le matériel. On peut le comparer à un interprète traduisant automatiquement le langage de Windows dans celui de la carte d'affichage.

# Setup CUDA DRIVER GPU PyTorch
- Exécuter les 2 script python pour verifier la config GPU, Driver et CUDA
“ python check_cuda_torch_device.py “ et “ python collect_env “
- ``` nvidia-smi ``` et ``` nvcc --version ``` et ``` python -m torch.utils.collect_env ``` pour d’autres infos
- [tuto](https://stackoverflow.com/questions/60987997/why-torch-cuda-is-available-returns-false-even-after-installing-pytorch-with) pour voir si GPU et Driver supportent la version de CUDA 

## Config:
- Windows 10 professionnel 64bit
- Processeur: Intel(R) Xeon(R) W-2123 CPU @ 3.60GHz
- RAM: 128 Go (128 Go utilisable)
- GPU: NVIDIA Quadro RTX 5000 (device 0)
- NVIDIA-SMI 462.31    Driver Version: 462.31   CUDA Version: 11.2 (min driver >=456.38) 

Note: The CUDA Version displayed in this table does not indicate that the CUDA toolkit or runtime are actually installed on your system. This just indicates the latest version of CUDA your graphics driver is compatible with.

CUDA runtime version: 10.0.130
Cuda compilation tools, release 10.0, V10.0.130
Location:
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA
Graphic Card support CUDA version
CUDA SDK 10 to 11.4
support for compute capability 7.5 (3.0 – 8.6)

## MAJ SETUP:
### MAJ du driver: NVIDIA - Téléchargements de pilotes 

- Driver installé et mis à jour dans: C:\NVIDIA\DisplayDriver\466.47\Win10-DCH_64\International

- Cuda toolkit installé dans: C:\Users\STEFFA~1\AppData\Local\Temp\CUDA

- C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.3
“cuda_11.3.1_465.89_win10”

- CUDA DNN installé: “cudnn-11.3-windows-x64-v8.2.0.53” dont les contenus des dossier “libs”, “include” et “bin” sont a mettre dans les dossiers “libs”, “include” et “bin” du Cuda toolkit

- Si besoin d’ajouter des variables d’environnements: https://github.com/miyamotok0105/unity-ml-agents/blob/master/docs/Installation-Windows.md
