```batch
 @echo off
 echo [LAUNCHER] Ativando o ambiente Conda e executando o Sanity Check...
 call C:\Users\limac\miniconda3\Scripts\activate.bat C:\Users\limac\miniconda3\envs\project-env
 python -i "C:\Users\limac\Documents\OpendTect_ML_Models\mlmodel_delta_pinn.py"
 pause
 ```
 *   **O que este script faz:**
     *   `@echo off`: Limpa o terminal.
     *   `echo ...`: Imprime uma mensagem de diagnóstico.
     *   `call ... activate.bat ...`: Ativa o nosso ambiente `project-env` corretamente.
     *   `python -i ...`: Executa o nosso script de teste em modo interativo.
     *   `pause`: Mantém a janela do terminal aberta no final para que possamos ler a saída.