function findOddNames(list) {
  // Filter developers with odd name sums
  const oddNamesDevelopers = list.filter(dev => {
    const firstNameSum = dev.firstName.split('').reduce((sum, char) => sum + char.charCodeAt(0), 0);
    return firstNameSum % 2 !== 0;
  });

  return oddNamesDevelopers;
}

// Example usage:
var list1 = [
  { firstName: 'Aba', lastName: 'N.', country: 'Ghana', continent: 'Africa', age: 21, language: 'Python' },
  { firstName: 'Abb', lastName: 'O.', country: 'Israel', continent: 'Asia', age: 39, language: 'Java' }
];

var result = findOddNames(list1);
console.log(result);