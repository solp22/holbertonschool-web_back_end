export default function signUpUser(firstName, lastName) {
  return new Promise(((myResolve, myReject) => {
    myResolve({
      firstName,
      lastName,
    });
    if (myReject) {
      throw new Error('Error');
    }
  }));
}
