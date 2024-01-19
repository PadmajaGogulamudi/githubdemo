function sortByLanguage(list) {
  return list.sort((a, b) => {
    // First, compare programming languages
    const languageComparison = a.language.localeCompare(b.language);

    // If programming languages are the same, compare first names
    if (languageComparison === 0) {
      return a.firstName.localeCompare(b.firstName);
    }

    return languageComparison;
  });
}

// Example usage:
var list1 = [  
  { firstName: 'Nikau', lastName: 'R.', country: 'New Zealand', continent: 'Oceania', age: 39, language: 'Ruby' },
  { firstName: 'Precious', lastName: 'G.', country: 'South Africa', continent: 'Africa', age: 22, language: 'JavaScript' },
  { firstName: 'Maria', lastName: 'S.', country: 'Peru', continent: 'Americas', age: 30, language: 'C' },
  { firstName: 'Agustin', lastName: 'V.', country: 'Uruguay', continent: 'Americas', age: 19, language: 'JavaScript' }
];

var sortedList = sortByLanguage(list1);
console.log(sortedList);