# this script takes a filename as a command line argument
# each line in file is a path/filename of the file to be killed

# https://stackoverflow.com/questions/10929453/read-a-file-line-by-line-assigning-the-value-to-a-variable
# https://stackoverflow.com/questions/5142429/unix-how-to-delete-files-listed-in-a-file

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "going to kill: $line"
    rm -rf "$line"
done < "$1"

