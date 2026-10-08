#!/bin/bash

# ==============================================================================
# SYSTEMIND TECH SOLUTIONS - LIGHTWEIGHT AUTOMATED SYSTEM HEALTH CHECK
# ==============================================================================
# Purpose: Quick system diagnostic script for IT Support & DevOps testing.
# Run with: chmod +x syscheck.sh && ./syscheck.sh
# ==============================================================================

clear
echo -e "\e[1;36m==================================================\e[0m"
echo -e "\e[1;32m      ⚡ SYSTEMIND AUTOMATED DIAGNOSTIC REPORT ⚡   \e[0m"
echo -e "\e[1;36m==================================================\e[0m"
echo -e "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
echo -e "OS Version: $(hostnamectl | grep "Operating System" | cut -d: -f2- | sed 's/^[ \t]*//')"
echo -e "Kernel: $(uname -r)"
echo -e "\e[1;36m--------------------------------------------------\e[0m"

# 1. STORAGE AUDIT (Checks for failing/full mounts)
echo -e "\n\e[1;34m[+] Storage & Disk Usage:\e[0m"
df -h --output=source,fstype,size,used,avail,pcent,target -x tmpfs -x devtmpfs | grep -E '^/dev/' || echo "No physical drives mounted."

# 2. RUNTIME RESOURCE ALLOCATION (Checks memory limits & active load)
echo -e "\n\e[1;34m[+] Memory Allocation & Load Average:\e[0m"
free -h | awk 'NR==1{print "       "$1"       "$2"       "$3} NR==2{print "RAM:   "$2"     "$3"     "$4}'
echo -e "System Load (1/5/15 mins): $(cat /proc/loadavg | awk '{print $1", "$2", "$3}')"

# 3. CONTAINER NETWORK STACK (Checks isolated microservices)
echo -e "\n\e[1;34m[+] Active Docker Containers:\e[0m"
if command -v docker &> /dev/null; then
    docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}\t{{.Ports}}"
else
    echo -e "\e[1;31m[!] Docker engine is not running or installed on this system.\e[0m"
fi

# 4. NETWORK BOUNDARY GATEWAY (Validates external packet flow)
echo -e "\n\e[1;34m[+] Core Connectivity Check:\e[0m"
ping -c 2 -W 3 8.8.8.8 &> /dev/null
if [ $? -eq 0 ]; then
    echo -e "\e[1;32m[✓] External Gateway Access: SUCCESS (Internet Connected)\e[0m"
else
    echo -e "\e[1;31m[✕] External Gateway Access: FAILED (Check hardware link / local routing table)\e[0m"
fi

echo -e "\n\e[1;36m==================================================\e[0m"
echo -e "\e[1;32m          DIAGNOSTIC AUTOMATION COMPLETE          \e[0m"
echo -e "\e[1;36m==================================================\e[0m"

