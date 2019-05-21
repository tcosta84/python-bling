# Bling ERP API Wrapper

A simple Python API Wrapper for [Bling ERP](https://bling.com.br/).

## Install

Via Pip:

``` bash
$ pip install bling
```

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

## Testing

``` bash
$ make test
```

## Security

If you discover any security related issues, please email thiagodacostabr@gmail.com instead of using the issue tracker.

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

## Credits

- [Thiago Costa][link-author]
- [All Contributors][link-contributors]

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.

[link-author]: https://twitter.com/goathi
[link-contributors]: ../../contributors