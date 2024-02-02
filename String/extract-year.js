var result = "";
var inputString = "1-2024"; // Replace undefined with your actual input

if (inputString !== undefined) {
    // Regular expression to match the year pattern (4 digits)
    const yearRegex = /\b(\d{4})\b/;

    // Extracting the year using match
    const match = inputString.match(yearRegex);

    // Check if a match is found
    if (match) {
        const year = match[1]; // The first capturing group contains the year
        result = year;
    } else {
        result = null;
    }
} else {
    result = null;
}

console.log(result); // Logs the extracted year or null
