#include <node.h>
#include <v8.h>
#include <Aria.h>

using namespace v8;

void Method(const v8::FunctionCallbackInfo<Value>& args) {
  Isolate* isolate = Isolate::GetCurrent();
  HandleScope scope(isolate);
  ArRobot* robot = new ArRobot();
  Aria::init();
  ArLog::init(ArLog::StdErr, ArLog::Normal, "", false, false, false);
  int argc = 0;
  char **argv = (char**)malloc(16*sizeof(char*));
  ArArgumentParser argParser(&argc, argv);
  argParser.loadDefaultArguments();
  ArRobotConnector* robotConnector = new ArRobotConnector(&argParser, robot);
  Aria::parseArgs();
  args.GetReturnValue().Set(String::NewFromUtf8(isolate, "world"));
}

void Init(Handle<Object> exports) {
  Isolate* isolate = Isolate::GetCurrent();
  exports->Set(String::NewFromUtf8(isolate, "hello"),
      FunctionTemplate::New(isolate, Method)->GetFunction());
}

NODE_MODULE(hello, Init)
