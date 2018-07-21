#include <ros/ros.h>
#include <speech_pkg/mode_srv.h>

using namespace ros;

bool getcommand(speech_pkg::mode_srv::Request &req, speech_pkg::mode_srv::Response &resp)	//name getcommand can be changed.
{
	ROS_INFO_STREAM("Received command");
	switch (req.comm)
	{
		case 'a' : 
			
		case 'b' :
		case 'c' :
		case 'd' :
		case 'e' :
	}
}


int main(int argc, char** argv)
{
	init(argc, argv, "botmaster");

	NodeHandle nh;

	ServiceServer server = nh.advertiseService("botmaster", &getcommand)	//name "botmaster" is to be changed.
	
	spin();

	return 0;
}