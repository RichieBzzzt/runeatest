from runeatest import pyspark
from runeatest import utils


def get_nunit_header(context):
    now = utils.get_date_and_time()
    print(now)
    now_date = now[0]
    now_time = now[1]
    nunit_header = '<test-results name="##name##" total="##total##" date="##getdate##" time="##gettime##">\n<environment nunit-version="2.6.0.12035" clr-version="2.0.50727.4963" os-version="Microsoft Windows NT 6.1.7600.0" platform="Win32NT" cwd="C:\\Program Files\\NUnit 2.6\\bin\\" machine-name="dummymachine" user="dummyuser" user-domain="dummy"/>\n<culture-info current-culture="en-US" current-uiculture="en-US"/>'
    nunit_header = (
        nunit_header.replace("##name##", context["extraContext"]["notebook_path"])
        .replace("##getdate##", now_date)
        .replace("##gettime##", now_time)
    )
    return nunit_header


def get_test_suite_results(results, context):
    test_suite_result = "success"
    test_suite_success = "True"
    for result in results:
        if result["result"] == "failure":
            test_suite_result = "failure"
            test_suite_success = "False"
    test_suite = '<test-suite type="TestFixture" name="##name##" executed="True" result="##test_suite_result##" success="##test_suite_success##" time="0.000" asserts="0"><results>'
    test_suite = (
        test_suite.replace("##name##", context["extraContext"]["notebook_path"])
        .replace("##test_suite_result##", test_suite_result)
        .replace("##test_suite_success##", test_suite_success)
    )
    return test_suite


def get_test_case_results(results):
    test_cases = []
    for result in results:
        if result["result"] == "failure":
            test_case_result = '<test-case name="##test##" description="" executed="True" result="##result##" success="##issuccess##" time="0.000" asserts="1">\n<failure>\n</failure>\n</test-case>'
        elif result["result"] == "success":
            test_case_result = '<test-case name="##test##" description="" executed="True" result="##result##" success="##issuccess##" time="0.000" asserts="1"/>'
        test_case_result = (
            test_case_result.replace("##test##", result["test"])
            .replace("##result##", result["result"])
            .replace("##issuccess##", result["issuccess"])
        )
        test_cases.append(test_case_result)
    print(test_cases)
    return test_cases


def get_nunit_footer():
    nunit_footer = "</results>\n</test-suite>\n</test-results>"
    return nunit_footer


def convert_to_nunit_results_format(testresults):
    context = pyspark.get_context()
    h = get_nunit_header(context)
    s = get_test_suite_results(testresults, context)
    f = get_nunit_footer()
    return h + s + f
