# Bling ERP API Wrapper

A simple Python API Wrapper for [Bling ERP](https://bling.com.br/).

## Install

Via Pip:

Not available yet.

Via GIT:

``` bash
$ pip install git+https://git@github.com/tcosta84/python-bling.git
```

## Usage

``` python

from bling import Api, ApiError

api = Api('your-api-key')

try:
	invoices = api.get_invoices(issued_date=['01/05/2019', '31/05/2019'], situation=7, type='S')
	for invoice in invoices:
		print(invoice['numero'])
except ApiError as e:
	print(e.response)

```

## Issues

Issues or new features can be reported via the [issue tracker](https://github.com/tcosta84/python-bling/issues). Please make sure your issue or feature has not yet been reported by anyone else before submitting a new one.

## Contributing

Clone the repository:

``` bash
$ git clone https://github.com/tcosta84/python-bling.git
```

Create an environment (e.g. with pyenv):

``` bash
$ pyenv virtualenv bling
$ pyenv activate
```

Configure development requirements:

``` bash
$ pip install -r requirements.txt
```

Testing:

``` bash
$ make test
```

## Credits

- [Thiago Costa][link-author]
- [All Contributors][link-contributors]

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.

[link-author]: https://twitter.com/goathi
[link-contributors]: ../../contributors