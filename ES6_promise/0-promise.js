export default function getResponseFromAPI() {
    return new Promise(function(myResolve, myReject) {
        myResolve({ message: 'OK' })
        if (myReject) {
            throw new Error('Error');
        }
    });
}