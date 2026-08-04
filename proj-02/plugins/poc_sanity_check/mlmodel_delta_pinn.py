# ==============================================================================
# OpendTect Machine Learning Model
# NOME: Delta-PINN Sanity Check
# TIPO: Prova de Conceito
# ==============================================================================

import torch

# O OpendTect procura por uma função 'do_apply' ou similar para execução.
# Por agora, vamos apenas provar que o arquivo é encontrado e pode ser importado.

def get_model_info():
    """
    Esta função pode ser chamada pelo OpendTect para obter informações sobre o modelo.
    """
    return {
        'name': 'Delta-PINN Sanity Check',
        'description': 'Valida a integração do ambiente Conda e o acesso à GPU.',
        'type': 'Other'
    }

def run_gpu_test():
    """
    Nossa função de teste, que podemos chamar mais tarde.
    """
    print("=============================================")
    print(">>> Plugin Delta-PINN: Iniciando Sanity Check...")
    print("=============================================")
    try:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"  -> Dispositivo mapeado: {device.type.upper()}")
        if device.type != 'cuda':
            raise RuntimeError("GPU CUDA não encontrada.")
        
        test_tensor = torch.randn(2, 2, device=device)
        print(f"  -> Tensor alocado na VRAM com sucesso.")
        print("\n>>> VEREDITO: SUCESSO ABSOLUTO <<<")
        
    except Exception as e:
        print(f"\n>>> VEREDITO: FALHA CRÍTICA: {e} <<<")
    
    print("=============================================")

# Este bloco é executado quando o Python importa o arquivo.
# É o nosso teste mais simples para ver se o OpendTect está nos "enxergando".
print("[Delta-PINN] Módulo 'mlmodel_delta_pinn.py' carregado com sucesso pelo OpendTect.")
run_gpu_test()