import os

lambda_path = "C:\\WG Git\\wgc-dark-web-proxy-svc\\application\\src\\breach_info\\app.py"



def test_lambda(event, context):
    try:
        os.system(f"python {lambda_path}")
    except Exception as e:
        print(e)


def main():

    test_lambda(None, None)

if __name__ == "__main__":
    main()