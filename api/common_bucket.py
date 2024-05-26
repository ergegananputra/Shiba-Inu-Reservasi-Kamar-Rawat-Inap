from typing import Union, List
from fastapi import Depends, HTTPException, APIRouter

from schemas.responses import BaseResponse
from sqlalchemy.orm import Session