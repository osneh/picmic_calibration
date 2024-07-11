lastFile=$(ls ../files/combinedPulseDigital_VRefN-SCAN_New11Jul2024_CalibrationIadj_VRefN_41_NOTDUMMIES_reducedIMADedit.csv | grep NOTDUMMIES | sort -r |  awk 'NR==2 { print; } END { print; }' | head -n1)
scanFile=$(ls /group/picmic/RUNDATA/TCPdata/*RefP-SCAN.csv)
echo $lastFile
echo "----------------------"
echo $scanFile
echo "----------------------"
python sweeping.py -fcali $lastFile -fscan $scanFile -sweeping 'False'
