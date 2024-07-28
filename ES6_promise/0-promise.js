export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const x = 'que mierda este tema';
    if (x) {
      resolve('Success');
    } else {
      reject(Error('Error'));
    }
  });
}
