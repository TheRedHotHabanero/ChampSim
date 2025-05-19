import re
from pathlib import Path
from typing import List, Dict

def parse_simulation_output(file_path: Path) -> Dict[str, float]:
    stats = {
        "trace": str(file_path)[48:],
        "IPC": None,
        "MPKI": None
    }

    with file_path.open() as f:
        for line in f:
            if match := re.search(r"CPU 0 cumulative IPC: ([\d.]+) instructions: (\d+) cycles: (\d+)", line):
                stats["IPC"] = float(match[1])
            elif match := re.search(r"Branch Prediction Accuracy: [\d.]+% MPKI: ([\d.]+)", line):
                stats["MPKI"] = float(match[1])

    return stats

def parse_multiple_traces(trace_files: List[str]) -> List[Dict[str, float]]:
    return [parse_simulation_output(Path(file)) for file in trace_files]

# Пример использования:
if __name__ == "__main__":
    trace_paths = [
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/600.perlbench_s-1273B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/602.gcc_s-1850B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/603.bwaves_s-2931B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/605.mcf_s-1536B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/607.cactuBSSN_s-2421B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/619.lbm_s-2676B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/620.omnetpp_s-141B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/621.wrf_s-575B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/623.xalancbmk_s-165B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/625.x264_s-12B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/627.cam4_s-490B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/628.pop2_s-17B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/631.deepsjeng_s-928B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/638.imagick_s-10316B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/641.leela_s-149B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/644.nab_s-12459B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/648.exchange2_s-387B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/649.fotonik3d_s-1176B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/654.roms_s-293B.txt",
        "/home/karina/prog/ChampSim/homeworks/homework_1/model_2/657.xz_s-4994B.txt"
    ]
    results = parse_multiple_traces(trace_paths)
    for stat in results:
        print(stat)
