logfile='run.log'

# timer
start_time="$(date -u +%s)"

for fol in qha_??.???
do echo Enter $fol
    cd $fol

    # perform phonopy calculation
    echo run phonopy
    vibes run phonopy >> $logfile
    echo "elapsed: $(($(date -u +%s)-$start_time))s"

    # perform postprocess
    vibes output phonopy phonopy/trajectory.son --full >> $logfile

    # perform reference aims calculation
    echo run aims
    vibes run singlepoint >> $logfile
    echo "elapsed: $(($(date -u +%s)-$start_time))s"
    # next
    cd ..
done

