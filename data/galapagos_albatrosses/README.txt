README

This data file is published by the Movebank Data Repository (www.datarepository.movebank.org). As of the time of publication, a version of the published animal tracking data set can be viewed on Movebank (www.movebank.org) in the study "Galapagos Albatrosses". Individual attributes in the data files are defined below and in the Movebank Attribute Dictionary, available at www.movebank.org/node/2381.

This data package includes the following data files:
Galapagos Albatrosses.csv
Galapagos Albatrosses-reference data.csv

These data are described in the following written publication:
Dodge, S., Bohrer, G., Weinzierl, R., Davidson, S.C., Kays, R., Douglas, D., Cruz, S., Han, J., Brandes, D., Wikelski, M., 2013, The Environmental-Data Automated Track Annotation (Env-DATA) System--Linking animal tracks with environmental data: Movement Ecology, v. 1:3. doi:10.1186/2051-3933-1-3

Data package citation
Cruz, S., Proaño, C.B., Anderson, D., Huyvaert, K., Wikelski, M., 2013, Data from: The Environmental-Data Automated Track Annotation (Env-DATA) System--Linking animal tracks with environmental data: Movebank Data Repository. doi:10.5441/001/1.3hp3s250

-----------

Terms of Use
This data file is licensed by the Creative Commons Zero (CC0 1.0) license. The intent of this license is to facilitate the re-use of works. The Creative Commons Zero license is a "no rights reserved" license that allows copyright holders to opt out of copyright protections automatically extended by copyright and other laws, thus placing works in the public domain with as little legal restriction as possible. However, works published with this license must still be appropriately cited following professional and ethical standards for academic citation.

We highly recommend that you contact the data creator if possible if you will be re-using or re-analyzing data in this file. Researchers will likely be interested in learning about new uses of their data, might also have important insights about how to properly analyze and interpret their data, and/or might have additional data they would be willing to contribute to your project. Feel free to contact us at support@movebank.org if you need assistance contacting data owners.

See here for the full description of this license
http://creativecommons.org/publicdomain/zero/1.0

-----------

Data Attributes
These definitions come from the Movebank Attribute Dictionary, available at www.movebank.org/node/2381.

animal comments: Additional information about the animal that is not described by other reference data terms.
	example: sibling of #1423

animal ID: An individual identifier for the animal, provided by the data owner. This identifier can be a ring number, a name, the same as the associated tag ID, etc. If the data owner does not provide an Animal ID, an internal Movebank animal identifier may sometimes be shown.
	example: 91876A, Gary
	same as: individual local identifier

animal life stage: The age class or life stage of the animal at the beginning of the deployment. Can be years or months of age or terms such as "adult", "subadult" and "juvenile". Units should be defined in the values (e.g. "2 years").
	example: juvenile, adult
	units: Any units should be defined in the remarks.

attachment type: The way a tag is attached to an animal. Values are chosen from a controlled list:
		collar: The tag is attached by a collar around the animal's neck.
		glue: The tag is attached to the animal using glue.
		harness: The tag is attached to the animal using a harness.
		implant: The tag is placed under the skin of the an animal.
		tape: The tag is attached to the animal using tape.
		other: user specified

deployment comments: Additional information about the tag deployment that is not described by other reference data terms.
	example: This deployment was excluded from analysis because the tag failed.

deploy on latitude: The geographic latitude of the location where the animal was released (intended primarily for instances in which the animal release and tag retrieval locations have higher accuracy than those derived from sensor data).
	example: 27.3516
	units: decimal degrees, WGS84 reference system

deploy on longitude: The geographic longitude of the location where the animal was released (intended primarily for instances in which the animal release and tag retrieval locations have higher accuracy than those derived from sensor data).
	example: -97.3321
	units: decimal degrees, WGS84 reference system

deploy on timestamp: The timestamp when the tag deployment started.
	example: 2008-08-33 18:00:00.000
	format: yyyy-MM-dd HH:mm:ss.sss
	units: UTC (Coordinated Universal Time) or GPS time, which is a few leap seconds different from UTC
	same as: deploy on date

duty cycle: Remarks associated with the duty cycle of a tag during the deployment, describing the times it is on/off and the frequency at which it transmits or records data.
	example: it turns off during the night
	units: Any units should be defined in the remarks.

e-obs battery voltage: Unloaded battery voltage (definition from Franz Kümmeth, e-obs Digital Telemetry, personal communication, 2012).
	example: 3712
	units: millivolt (mV)

e-obs fix battery voltage: Loaded battery voltage, i.e. battery voltage when GPS module is acquiring a fix (definition from e-obs Digital Telemetry Manual for DataDecoder Software, 2010; Franz Kümmeth, e-obs Digital Telemetry, personal communication, 2012).
	example: 3535
	units: millivolt (mV)

e-obs horizontal accuracy estimate: A horizontal (in)accuracy estimate, calculated by the GPS module (definition from e-obs Digital Telemetry Manual for DataDecoder Software, 2010; Franz Kümmeth, e-obs Digital Telemetry, personal communication, 2012).
	example: 35.07
	units: meters

e-obs key bin checksum: A checksum of the original binary data, so that Movebank can quickly compare different lines by comparing their checksums (definition from "e-obs GPS-acceleration-tags application note: How to use the acceleration sensor, interpret, analyse its data and how to get values in m/s^2", 2011).
	example: 4152324118
	units: none

e-obs speed accuracy estimate: A speed (in)accuracy estimate, calculated by the GPS module. The speed accuracy estimate (better named "inaccuracy estimation")  may show very high values, since the GPS module calculates a very conservative value. These speed measurements are potentially very inaccurate when interpreting the data (definition from e-obs Digital Telemetry Manual for DataDecoder Software, 2010; Franz Kümmeth, e-obs Digital Telemetry, personal communication, 2012).
	example: 6.58
	units: meters per second

e-obs start timestamp: The date and time of day when the acceleration burst belonging to this line begins. The exact time of the first sample is a little later (up to 1 second) for older e-obs tags, especially when the ACC-pinger is enabled (4 pings before the start of eah ACC burst) (definition from "e-obs GPS-acceleration-tags application note: How to use the acceleration sensor, interpret, analyse its data and how to get values in m/s^2", 2011).
	example: 2011-01-03 13:45:00.000
	units: GPS time (GPST), which is a few leap seconds different from UTC (Coordinated Universal Time)

e-obs status: The record status, from e-obs GPS/accelerometer tags (definition from e-obs Digital Telemetry Manual for DataDecoder Software, 2010). Allowed values are
		A = position and time within accuracy masks
		B = only time of week and weeknumber valid
		C = only weeknumber valid
		D = no valid data
	example: D
	units: none

e-obs temperature: Temperature; this value is not calibrated and therefore very inaccurate (definition from e-obs Digital Telemetry Manual for DataDecoder Software, 2010).
	example: 45
	units: degrees Celsius

e-obs type of fix: The type of fix of data from e-obs GPS/accelerometer tags (definition from e-obs Digital Telemetry Manual for DataDecoder Software, 2010). Allowed values are
		3 = 3D fix
		2 = 2D fix
	example: 3
	units: none

e-obs used time to get fix: The amount of time that was needed for this GPS fix; interesting for estimating power requirements (definition from e-obs Digital Telemetry Manual for DataDecoder Software, 2010).
	example: 22
	units: seconds

event ID: An identifier for the set of information associated with each record or event in a data set. A unique event ID is assigned to every time-location or other time-measurement record in Movebank.
	example: 6340565
	units: none

ground speed: The estimated ground speed between consecutive locations.
	example: 7.22
	units: meters per second

heading: The direction in which the tag moved from this location to the subsequent location, calculated as the bearing between consecutive locations, in decimal degrees clockwise from north; for example, 0 = north, 90 = east, 180 = south.
	example: 315.88
	units: decimal degrees

height above ellipsoid: The height above the ellipsoid returned by the GPS unit.
	example: 24.8
	units: meters

latitude (decimal degree): The geographic longitude of a location along an animal track as estimated by the processed sensor data. Positive values are east of the Greenwich Meridian, negative values are west of it.
	example: -121.1761111
	units: decimal degrees, WGS84 reference system
	same as: location lat

latitude (UTM): The geographic longitude of the geographic center of a location along an animal track as estimated by the processed sensor data.
	example: 3628361.84012295
	units: meters, WGS84 reference system
	same as: utm northing

local timestamp: The date and time a sensor measurement was taken in the time zone of the study reference location.
	example: 2008-08-14 15:31:00.000
	format: yyyy-MM-dd HH:mm:ss.sss
	units: specific to the study time zone
	same as: study local timestamp

longitude (decimal degree): The geographic longitude of a location along an animal track as estimated by the processed sensor data. Positive values are east of the Greenwich Meridian, negative values are west of it.
	example: -121.1761111
	units: decimal degrees, WGS84 reference system
	same as: location long

longitude (UTM): The geographic longitude of the geographic center of a location along an animal track as estimated by the processed sensor data.
	example: 756243.7836
	units: meters, WGS84 reference system
	same as: utm easting

manipulation type: The way in which the animal was manipulated during the deployment. Additional details about the manipulation can be provided using manipulation comments. Values are chosen from a controlled list:
	confined: The animal's movement was restricted to within a defined area.
	none: The animal received no treatment other than the tag attachment.
	relocated: The animal was released from a site other than the one at which it was captured.
	manipulated other: The animal was manipulated in some other way, such as a physiological manipulation.

sensor type: The type of sensor with which data were collected.
Values are chosen from a controlled list:
		acceleration: The sensor collects acceleration data.
		accessory measurements: The sensor collects accessory measurements, such as battery voltage.
		Argos Doppler Shift: The sensor is using Argos Doppler shift for determining position.
		bird ring: The animal is identified by a ring that has a unique ID.
		GPS: The sensor uses GPS to find location and stores these.
		natural mark: The animal is identified by a natural marking.
		radio transmitter: The sensor is a classical radio transmitter.
		solar geolocator: The sensor collects light levels, which are used to determine position (for processed locations).
		solar geolocator raw: The sensor collects light levels, which are used to determine position (for raw light-level measurements).

study name: The name of the study in Movebank in which data are stored.

study site: The name of the deployment site, for example a field station or colony.
	example: Pickerel Island North

study time zone: The time zone at the study reference location.
	example: Mountain Standard Time
	units: none

tag ID: A unique identifier for the tag, provided by the data owner. If the data owner does not provide a tag ID, an internal Movebank tag identifier may sometimes be shown.
	example: 2342, ptt_4532
	same as: tag local identifier

tag manufacturer name: The company or person that produced the tag.
	example: Holohil
	same as: manufacturer

tag mass: The mass of the tag.
	example: 24
	units: grams

tag readout method: The way the data are received from the tag. Values are chosen from a controlled list:
		satellite: Data are transferred via satellite.
		phone network: Data are transferred via a phone network, such as GSM or AMPS.
		other wireless: Data are transferred via another form of wireless data transfer, such as a VHF radio transmitter/receiver.
		tag retrieval: The tag must be physically retrieved in order to obtain the data.

taxon: The scientific name of the species on which the tag was deployed, as defined by the Integrated Taxonomic Information System (ITIS, www.itis.gov). If the species name can not be provided, this should be the lowest level taxonomic rank that can be determined and that is used in the ITIS taxonomy. Additional information can be provided using the term taxon detail.
	example: Buteo swainsoni
	same as: species, animal taxon, individual taxon canonical name

timestamp: The date and time a sensor measurement was taken.
	example: 2008-08-14 18:31:00.000
	format: yyyy-MM-dd HH:mm:ss.sss
	units: UTC (Coordinated Universal Time) or GPS time, which is a few leap seconds different from UTC

UTM zone: The UTM zone, selected based on the location of each event, used to convert locations from decimal degrees to UTM.
	example: 14N
	units: none

visible: Determines whether an event is visible on the Movebank Search map. Values are calculated automatically, with FALSE indicating that the event has been marked as an outlier by manually marked outlier or algorithm marked outlier. Allowed values are TRUE or FALSE.

-----------

More Information
For more information about this repository, see the FAQ at www.movebank.org/node/2220 or contact us at support@movebank.org.