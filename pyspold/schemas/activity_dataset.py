from pydantic import BaseModel, Field
from pyspold.schemas.modelling_and_validation.modelling_and_validation import ModellingAndValidation

from pyspold.schemas.activity_description.activity_description import ActivityDescription
from pyspold.schemas.administrative_information.administrative_information import AdministrativeInformation
from pyspold.schemas.flow_data.flow_data import FlowData


class ActivityDataset(BaseModel):
    activity_description: ActivityDescription = Field(alias="activityDescription")
    flow_data: FlowData = Field(alias="flowData")
    modelling_and_validation: ModellingAndValidation = Field(
        alias="modellingAndValidation",
    )
    administrative_information: AdministrativeInformation = Field(
        alias="administrativeInformation",
    )
