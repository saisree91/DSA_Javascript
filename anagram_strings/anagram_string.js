let str1 = prompt("Enter string1");
let str2 = prompt("Enter string2");
let n = 0;
let str1_arr = str1.split('').sort().join('');
let str2_arr = str2.split('').sort().join('');
let str1_len = str1.length;
let str2_len = str2.length;
if (str1.len != str2.len) {
    document.write("Strings are not Anagram");
}
else {
    for (let i = 0; i < str1_len; i++) {
        if (str1_arr[i] != str2_arr[i]) {
            n -= 1;
        }
        else {
            n += 1;
        }
    }
}

if (n === str1_len) {
    document.write("Strings are anagram");
}
else {
    document.write("Strings are not anagram");
}
