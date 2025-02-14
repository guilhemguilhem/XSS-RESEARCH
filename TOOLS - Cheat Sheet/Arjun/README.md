### What's Arjun?

Arjun can find query parameters for URL endpoints. If you don't get what that means, it's okay, read along.

Web applications use parameters (or queries) to accept user input, take the following example into consideration

`http://api.example.com/v1/userinfo?id=751634589`

This URL seems to load user information for a specific user id, but what if there exists a parameter named `admin` which when set to `True` makes the endpoint provide more information about the user?  
This is what Arjun does, it finds valid HTTP parameters with a huge default dictionary of 25,890 parameter names.

The best part? It takes less than 10 seconds to go through this huge list while making just 50-60 requests to the target. [Here's how](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F).

### [](https://github.com/s0md3v/Arjun#why-arjun)Why Arjun?

-   Supports `GET/POST/POST-JSON/POST-XML` requests
-   Automatically handles rate limits and timeouts
-   Export results to: BurpSuite, text or JSON file
-   Import targets from: BurpSuite, text file or a raw request file
-   Can passively extract parameters from JS or 3 external sources

### [](https://github.com/s0md3v/Arjun#installing-arjun)Installing Arjun

You can install `arjun` with pip as following:

```
pip3 install arjun
```

or, by downloading this repository and running

```
python3 setup.py install
```

### [](https://github.com/s0md3v/Arjun#how-to-use-arjun)How to use Arjun?

A detailed usage guide is available on [Usage](https://github.com/s0md3v/Arjun/wiki/Usage) section of the Wiki.

Direct links to some basic options are given below:

-   [Scan a single URL](https://github.com/s0md3v/Arjun/wiki/Usage#scan-a-single-url)
-   [Import targets](https://github.com/s0md3v/Arjun/wiki/Usage#import-multiple-targets)
-   [Export results](https://github.com/s0md3v/Arjun/wiki/Usage#save-output-to-a-file)
-   [Use custom HTTP headers](https://github.com/s0md3v/Arjun/wiki/Usage#use-custom-http-headers)

Optionally, you can use the `--help` argument to explore Arjun on your own.

##### [](https://github.com/s0md3v/Arjun#credits)Credits

The parameter names wordlist is created by extracting top parameter names from [CommonCrawl](http://commoncrawl.org) dataset and merging best words from [SecLists](https://github.com/danielmiessler/SecLists) and [param-miner](https://github.com/PortSwigger/param-miner) wordlists into that.  
`db/special.json` wordlist is taken from [data-payloads](https://github.com/yehgdotnet/data-payloads).