import time
import google.auth.crypt
import google.auth.jwt

sa_keyfile = 'dulce-demo-0ac2dabfe5b7.json'
iss = 'test-api@dulce-demo.iam.gserviceaccount.com'
aud = '959368492243-5bs8i25l6br96a19mar2bnhfg5u7blqs.apps.googleusercontent.com'
iat = int(time.time())
exp = iat + 3600


def generate_jwt():
    """Generates a signed JSON Web Token using a Google API Service Account."""
    payload = {"iat": iat, "exp": exp, "iss": iss, "aud":  aud, "sub": iss, "email": iss}

    signer = google.auth.crypt.RSASigner.from_service_account_file(sa_keyfile)
    jwt = google.auth.jwt.encode(signer, payload)
    return jwt


if __name__ == '__main__':
    signed_jwt = generate_jwt()
    print(signed_jwt.decode()+'\n')