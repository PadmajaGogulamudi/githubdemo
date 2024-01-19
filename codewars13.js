function isLanguageDiverse(list) {
  const languageCounts = list.reduce((counts, dev) => {
    counts[dev.language] = (counts[dev.language] || 0) + 1;
    return counts;
  }, {});
  const countsArray = Object.values(languageCounts);

  
  const maxCount = Math.max(...countsArray);
  const minCount = Math.min(...countsArray);
  return maxCount <= 2 * minCount;
}


var list1 = [
  { firstName: 'Daniel', lastName: 'J.', country: 'Aruba', continent: 'Americas', age: 42, language: 'Python' },
  { firstName: 'Kseniya', lastName: 'T.', country: 'Belarus', continent: 'Europe', age: 22, language: 'Ruby' },
  { firstName: 'Sou', lastName: 'B.', country: 'Japan', continent: 'Asia', age: 43, language: 'Ruby' },
  { firstName: 'Hanna', lastName: 'L.', country: 'Hungary', continent: 'Europe', age: 95, language: 'JavaScript' },
  { firstName: 'Jayden', lastName: 'P.', country: 'Jamaica', continent: 'Americas', age: 18, language: 'JavaScript' },
  { firstName: 'Joao', lastName: 'D.', country: 'Portugal', continent: 'Europe', age: 25, language: 'JavaScript' }
];

var result = isLanguageDiverse(list1);
console.log(result)