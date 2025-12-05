import time
import random
import sys
from datetime import datetime
from colorama import init, Fore, Style

# 初始化 colorama，autoreset=True
init(autoreset=True)

# intimidate your coworkers
LOG_MESSAGES = [
    "[Q-PROC] Stabilizing logical qubits via topological error correction codes... [Coherence: 99.992%]",
    "[ENTANGLEMENT] Teleporting quantum states across repeater nodes (Alice -> Bob protocol). Verification pending...",
    "[ANNEALING] Minimizing Hamiltonian energy landscape for combinatorial optimization problem...",
    "[CRYO-SYS] Dilution refrigerator temperature holding at 15mK. Superconducting pathways active.",
    "[SIMULATION] Solving Schrödinger equation for multi-electron systems using Hartree-Fock method...",
    "[NEURAL-NET] Pruning synaptic weights in hidden layers 2048-4096 for sparsity optimization...",
    "[TRAINING] Backpropagating gradients on 175B parameter Transformer model. Epoch 42/1000. [Loss: 0.0034]",
    "[TENSOR-OPS] Offloading matrix multiplication to TPU Cluster v4-Pod. Compiling XLA kernels...",
    "[INFERENCE] Quantizing floating-point weights to INT8 for edge-device acceleration...",
    "[AGI-CORE] Synthesizing natural language context vectors from unstructured data lakes...",
    "[SEC-OPS] Verifying Zero-Knowledge Proofs (ZKP-SNARKs) for side-chain transactions...",
    "[CRYPTO] Generating Elliptic Curve Ephemeral Diffie-Hellman (ECDHE) keys for post-quantum security...",
    "[FIREWALL] Mitigating polymorphic DDoS attack vectors via active entropy analysis. Pattern identified.",
    "[PENTEST] Injecting fuzzing payloads into buffer overflow vulnerability at memory address 0x7FFF...",
    "[HASH-RATE] Mining nonce for block #849201. Hashrate peaking at 450 TH/s.",
    "[K8S-ORCH] Scaling pod replicas across multi-region availability zones (US-EAST / AP-NORTH).",
    "[DATA-LAKE] Ingesting petabyte-scale telemetry streams into columnar NVMe RAID arrays...",
    "[LATENCY] Re-routing high-frequency trading packets via Starlink-V2 low-orbit mesh... [Ping: <2ms]",
    "[COMPILER] JIT-compiling LLVM intermediate representation for AVX-512 instruction set...",
    "[KERNEL] Kernel panic averted. System entropy pool stabilized. Awaiting high-priority interrupt."
]

# 绿色、青色、白色
COLORS = [Fore.GREEN, Fore.CYAN, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RED]

def get_timestamp():
    """获取当前时间，精确到毫秒，看起来更专业"""
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]

def type_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # 每个字之间极短的随机延迟
        time.sleep(random.uniform(0.001, 0.03)) 
    print() # 换行

# 在主循环里调用：
# type_print(log_line)

def main():
    print(Fore.RED + Style.BRIGHT + ">>> INITIALIZING SYSTEM CORE...")
    print(Fore.RED + Style.BRIGHT + ">>> ESTABLISHING SECURE UPLINK...")
    time.sleep(2) # 假装启动需要时间
    print(Fore.GREEN + ">>> SYSTEM ONLINE.\n")
    
    try:
        while True:
            message = random.choice(LOG_MESSAGES)
            
            color = random.choice(COLORS)
            
            # 构造输出行：时间戳 + 消息
            # Style.BRIGHT 老式CRT显示器
            log_line = f"[{get_timestamp()}] {color}{Style.BRIGHT}{message}"
            
            type_print(log_line)
            
            delay_type = random.random()
            if delay_type < 0.1: 
                # 10% 的概率出现急速刷屏（极快）
                wait_time = random.uniform(0.05, 0.2)
            elif delay_type > 0.9:
                # 10% 的概率出现长耗时任务（显得很卡顿）
                wait_time = random.uniform(1.5, 3.0)
            else:
                # 正常速度
                wait_time = random.uniform(0.3, 1.0)
                
            time.sleep(wait_time)

    except KeyboardInterrupt:
        # high tech Ctrl+C 
        print(Fore.RED + "\n>>> INTERRUPT RECEIVED. SYSTEM SHUTTING DOWN.")
        print(Fore.RED + ">>> DATA BUFFER FLUSHED.")
        sys.exit()

if __name__ == "__main__":
    main()