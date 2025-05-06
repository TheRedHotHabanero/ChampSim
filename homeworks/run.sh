#!/bin/bash

TRACE_DIR="/home/karina/prog/ChampSim/homeworks/benchmarks"

RESULT_DIR="/home/karina/prog/ChampSim/homeworks/homework_2/lru"
mkdir -p "$RESULT_DIR"

TIMING_LOG="$RESULT_DIR/timing.log"
echo "Trace Simulation Timing Log" > "$TIMING_LOG"
echo "---------------------------" >> "$TIMING_LOG"

TRACE_LIST=(
    "600.perlbench_s-1273B.champsimtrace.xz"
    "602.gcc_s-1850B.champsimtrace.xz"
    "603.bwaves_s-2931B.champsimtrace.xz"
    "605.mcf_s-1536B.champsimtrace.xz"
    "607.cactuBSSN_s-2421B.champsimtrace.xz"
    "619.lbm_s-2676B.champsimtrace.xz"
    "620.omnetpp_s-141B.champsimtrace.xz"
    "621.wrf_s-575B.champsimtrace.xz"
    "623.xalancbmk_s-165B.champsimtrace.xz"
    "625.x264_s-12B.champsimtrace.xz"
    "627.cam4_s-490B.champsimtrace.xz"
    "628.pop2_s-17B.champsimtrace.xz"
    "631.deepsjeng_s-928B.champsimtrace.xz"
    "638.imagick_s-10316B.champsimtrace.xz"
    "641.leela_s-149B.champsimtrace.xz"
    "644.nab_s-12459B.champsimtrace.xz"
    "648.exchange2_s-387B.champsimtrace.xz"
    "649.fotonik3d_s-1176B.champsimtrace.xz"
    "654.roms_s-293B.champsimtrace.xz"
    "657.xz_s-4994B.champsimtrace.xz"
)

for trace_file in "${TRACE_LIST[@]}"; do
    trace_name=$(basename "$trace_file" .champsimtrace.xz)
    output_file="$RESULT_DIR/${trace_name}.txt"

    if [[ ! -f "$TRACE_DIR/$trace_file" ]]; then
        echo "File $TRACE_DIR/$trace_file does not exist. Skipping simulation for $trace_name."
        echo "[$(date +"%Y-%m-%d %H:%M:%S")] WARNING: File $TRACE_DIR/$trace_file does not exist. Skipping simulation for $trace_name." >> "$TIMING_LOG"
        continue
    fi

    start_time=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$start_time] Starting simulation for: $trace_name"
    echo "[$start_time] Starting simulation for: $trace_name" >> "$TIMING_LOG"

    script -q -c "/home/karina/prog/ChampSim/bin/champsim --warmup-instructions 10000000 --simulation-instructions 50000000 $TRACE_DIR/$trace_file" > "$output_file" 2>&1


    end_time=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$end_time] Finished simulation for: $trace_name"
    echo "[$end_time] Finished simulation for: $trace_name" >> "$TIMING_LOG"
    echo "----------------------------------------" >> "$TIMING_LOG"
done
