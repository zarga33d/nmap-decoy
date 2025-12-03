#!/bin/bash

# القيمة الافتراضية لملف الديكويز
decoy_file="decoylist.txt"

# التحقق من وجود وسيطات
if [ $# -lt 1 ]; then
  echo "Usage: $0 [--list <decoy_file>] <target_ip> [nmap options]"
  exit 1
fi

# معالجة الوسائط
while [[ $# -gt 0 ]]; do
  case "$1" in
    --list)
      shift
      if [ -z "$1" ]; then
        echo "Error: --list requires a filename"
        exit 1
      fi
      decoy_file="$1"
      shift
      ;;
    *)
      # أول وسيط غير مرتبط بـ --list هو الهدف
      target_ip="$1"
      shift
      break
      ;;
  esac
done

if [ -z "$target_ip" ]; then
  echo "Error: Target IP is required."
  exit 1
fi

# باقي الوسائط هي خيارات nmap إضافية
nmap_options="$@"

# قراءة الديكويز من الملف
if [ ! -f "$decoy_file" ]; then
  echo "Error: Decoy file '$decoy_file' not found."
  exit 1
fi

decoys=$(paste -sd "," "$decoy_file")
decoys="$decoys,ME"

echo "Scanning $target_ip with decoys from $decoy_file using options: $nmap_options"
sudo nmap -D $decoys $nmap_options "$target_ip"
