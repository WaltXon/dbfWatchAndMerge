import arcpy
import os

def plot(csv):

	arcpy.env.overwriteOutput = True
	arcpy.env.workspace = os.path.split(csv)[0]
	basename = os.path.basename(csv)[:-4]

	table = csv
	in_x_field = 'well_long'
	in_y_field = 'well_lat'
	out_layer = basename + '.lyr'
	spatial_reference = arcpy.SpatialReference(4269) #GCS_North_American_1983 = 4269 
													 #GCS_North_American_1927 = 4267
	arcpy.MakeXYEventLayer_management (table, in_x_field, in_y_field, out_layer, spatial_reference)

	in_features= out_layer
	out_feature_class = basename + '.shp'
	arcpy.CopyFeatures_management (in_features, out_feature_class)