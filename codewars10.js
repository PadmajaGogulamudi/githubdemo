function addUsername(inputArray) {
    const currentYear = new Date().getFullYear();

    return inputArray.map((obj) => {
        const birthYear = currentYear - obj.age;
        const username = `${obj.firstName.toLowerCase()}${obj.lastName.charAt(0).toLowerCase()}${birthYear}`;
        
        return { ...obj, username };
    });
}

// Example usage with the provided list1
var list1 = [
  { firstName: 'Emily', lastName: 'N.', country: 'Ireland', continent: 'Europe', age: 30, language: 'Ruby' },
  { firstName: 'Nor', lastName: 'E.', country: 'Malaysia', continent: 'Asia', age: 20, language: 'Clojure' }
];

var result = addUsername(list1);
console.log(result);