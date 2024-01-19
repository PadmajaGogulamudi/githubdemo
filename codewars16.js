function askForMissingDetails(inputArray) {
    return inputArray.filter((developer) => {
        const missingProperty = Object.keys(developer).find((key) => developer[key] === null);

        if (missingProperty) {
            const question = `Hi, could you please provide your ${missingProperty}.`;
            developer.question = question;
            return true;
        }

        return false;
    });
}

// Example usage with the provided list1
var list1 = [
    { firstName: null, lastName: 'I.', country: 'Argentina', continent: 'Americas', age: 35, language: 'Java' },
    { firstName: 'Lukas', lastName: 'X.', country: 'Croatia', continent: 'Europe', age: 35, language: null },
    { firstName: 'Madison', lastName: 'U.', country: 'United States', continent: 'Americas', age: 32, language: 'Ruby' }
];

var result = askForMissingDetails(list1);
console.log(result);