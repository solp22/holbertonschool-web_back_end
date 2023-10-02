export default function getResponseFromAPI() {
  return new Promise(((myResolve, myReject) => {
    myResolve({ message: 'OK' });
    if (myReject) {
      throw new Error('Error');
    }
  }));
}
