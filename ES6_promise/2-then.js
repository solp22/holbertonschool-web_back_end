export default function handleResponseFromAPI(promise) {
  return new Promise(((myResolve, myReject) => {
    myResolve({
      status: 200,
      body: 'success',
    });
    if (myReject) {
      throw Error();
    }
    promise.then(
      console.log('Got a response from the API'),
    );
  }));
}
