export default function hasValuesFromArray(set, array) {
  const exist = array.every((value) => set.has(value));

  if (exist) {
    console.log('true');
  } else {
    console.log('false');
  }
}
