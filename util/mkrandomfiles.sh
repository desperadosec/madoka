for n in {1..1000}; do
    dd if=/dev/urandom of=file$( printf %03d "$n" ).bin bs=1 count=$(( 5 + 1024))
done
